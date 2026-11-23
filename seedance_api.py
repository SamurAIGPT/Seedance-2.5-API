import os
import time

import requests
from dotenv import load_dotenv


load_dotenv()


_RESOLUTION_SUFFIXES = {
    None: "",
    "720p": "",
    "480p": "-480p",
    "1080p": "-1080p",
    "4k": "-4k",
}

_SEEDANCE_25_FAMILIES = (
    "text-to-video",
    "image-to-video",
    "first-last-frame",
    "omni-reference",
    "video-edit",
    "video-extend",
)

_SEEDANCE_25_VARIANTS = ("", "intl-", "spicy-")

SEEDANCE_25_ENDPOINTS = frozenset(
    "seedance-2.5-{}{}{}".format(variant, family, suffix)
    for variant in _SEEDANCE_25_VARIANTS
    for family in _SEEDANCE_25_FAMILIES
    for suffix in ("", "-480p", "-1080p", "-4k")
)

_FLASH_MODES = ("text-to-video", "image-to-video", "first-last-frame", "reference-to-video", "video-edit", "video-extend")

SEEDANCE_25_FLASH_ENDPOINTS = frozenset(
    "seedance-2.5-flash-{}{}".format(prefix, mode)
    for prefix in ("", "intl-", "spicy-")
    for mode in _FLASH_MODES
)


def _is_transient_status(response):
    """True for HTTP responses worth retrying while polling (429 and 5xx)."""
    return response is not None and (response.status_code == 429 or response.status_code >= 500)


class SeedanceAPI:
    """Small Python client for MuAPI's Seedance 2.5 route family."""

    def __init__(self, api_key=None, timeout=60, upload_timeout=300):
        """
        Initialize the Seedance 2.5 API client.

        :param api_key: MuAPI API key. Defaults to MUAPI_API_KEY.
        :param timeout: seconds to wait on each API request before giving up.
        :param upload_timeout: seconds to wait on a file upload.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor."
            )

        self.timeout = timeout
        self.upload_timeout = upload_timeout
        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    @staticmethod
    def _endpoint(family, variant="standard", resolution=None):
        """Build and validate one of the public Seedance 2.5 route slugs."""
        if variant == "standard":
            variant_prefix = ""
        elif variant in ("intl", "spicy"):
            variant_prefix = variant + "-"
        else:
            raise ValueError("variant must be 'standard', 'intl', or 'spicy'")

        normalized_resolution = resolution.lower() if isinstance(resolution, str) else resolution
        if normalized_resolution not in _RESOLUTION_SUFFIXES:
            raise ValueError("resolution must be one of: 480p, 720p, 1080p, or 4k")

        endpoint = "seedance-2.5-{}{}{}".format(
            variant_prefix,
            family,
            _RESOLUTION_SUFFIXES[normalized_resolution],
        )
        if endpoint not in SEEDANCE_25_ENDPOINTS:
            raise ValueError("Unsupported Seedance 2.5 endpoint: {}".format(endpoint))
        return endpoint

    @staticmethod
    def _endpoint_kind(endpoint):
        if endpoint.endswith("video-edit") or "video-edit-" in endpoint:
            return "video-edit"
        if endpoint.endswith("video-extend") or "video-extend-" in endpoint:
            return "video-extend"
        if endpoint.endswith("image-to-video") or "image-to-video-" in endpoint:
            return "image-to-video"
        if endpoint.endswith("first-last-frame") or "first-last-frame-" in endpoint:
            return "first-last-frame"
        if endpoint.endswith("omni-reference") or "omni-reference-" in endpoint:
            return "omni-reference"
        return "text-to-video"

    def generate(
        self,
        endpoint,
        prompt,
        aspect_ratio="16:9",
        duration=5,
        seed=None,
        image_url=None,
        images_list=None,
        videos_list=None,
        audios_list=None,
        video=None,
        reference_images=None,
        reference_audios=None,
        last_image=None,
        generate_audio=None,
        webhook_url=None,
    ):
        """
        Submit a request to any current Seedance 2.5 route.

        The endpoint must be one of :data:`SEEDANCE_25_ENDPOINTS`. Use the
        workflow-specific convenience methods below when you do not need to
        select a route dynamically.

        T2V uses ``prompt``. I2V adds ``image_url``. First & Last Frame uses
        exactly two ``images_list`` entries. Omni Reference accepts optional
        ``images_list``, ``videos_list``, and ``audios_list``. Video Edit uses
        ``video``, optional ``reference_images``/``reference_audios``, and
        ``generate_audio``. Video Extend uses ``video`` and optional
        ``last_image``.
        """
        if endpoint not in SEEDANCE_25_ENDPOINTS:
            raise ValueError("Unsupported Seedance 2.5 endpoint: {}".format(endpoint))

        kind = self._endpoint_kind(endpoint)
        if kind == "image-to-video" and not image_url:
            raise ValueError("image_url is required for Image-to-Video endpoints")
        if kind == "first-last-frame":
            if not images_list or len(images_list) != 2:
                raise ValueError("images_list must contain exactly two URLs")
        if kind in ("video-edit", "video-extend") and not video:
            raise ValueError("video is required for video edit and extend endpoints")

        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        if webhook_url is not None:
            payload["webhook_url"] = webhook_url

        if kind == "image-to-video":
            payload["image_url"] = image_url
        elif kind == "first-last-frame":
            payload["images_list"] = images_list
        elif kind == "omni-reference":
            if images_list:
                payload["images_list"] = images_list
            if videos_list:
                payload["videos_list"] = videos_list
            if audios_list:
                payload["audios_list"] = audios_list
        elif kind == "video-edit":
            payload["video"] = video
            if reference_images:
                payload["reference_images"] = reference_images
            if reference_audios:
                payload["reference_audios"] = reference_audios
            if generate_audio is not None:
                payload["generate_audio"] = generate_audio
        elif kind == "video-extend":
            payload["video"] = video
            if last_image:
                payload["last_image"] = last_image
            if generate_audio is not None:
                payload["generate_audio"] = generate_audio

        return self._post_request("{}/{}".format(self.base_url, endpoint), payload)

    # ------------------------------------------------------------------
    # Seedance 2.5 Flash (480p/720p, 4-30s, $0.114/s and $0.228/s; intl and spicy +10%)
    # ------------------------------------------------------------------
    def flash(self, mode, prompt, spicy=False, intl=False, **fields):
        """
        Submit a Seedance 2.5 Flash job.

        :param mode: one of text-to-video, image-to-video, first-last-frame,
            reference-to-video, video-edit, video-extend.
        :param spicy: use the relaxed-moderation ``seedance-2.5-flash-spicy-*`` route.
        :param intl: use the international (Dreamina) ``seedance-2.5-flash-intl-*`` route.
        :param fields: endpoint fields: ``resolution`` (480p/720p), ``duration`` (4-30),
            ``aspect_ratio``, ``generate_audio``, ``seed``, ``image_url``, ``images_list``,
            ``videos_list``, ``audios_list``, ``video_url``.
        """
        if mode not in _FLASH_MODES:
            raise ValueError("mode must be one of: {}".format(", ".join(_FLASH_MODES)))
        if spicy and intl:
            raise ValueError("choose spicy or intl, not both")
        endpoint = "seedance-2.5-flash-{}{}".format("spicy-" if spicy else "intl-" if intl else "", mode)
        payload = {"prompt": prompt}
        payload.update({k: v for k, v in fields.items() if v is not None})
        return self._post_request("{}/{}".format(self.base_url, endpoint), payload)

    def flash_text_to_video(self, prompt, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash text-to-video."""
        return self.flash("text-to-video", prompt, spicy, intl, **fields)

    def flash_image_to_video(self, prompt, image_url, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash image-to-video."""
        return self.flash("image-to-video", prompt, spicy, intl, image_url=image_url, **fields)

    def flash_first_last_frame(self, prompt, images_list, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash first & last frame (exactly two image URLs)."""
        return self.flash("first-last-frame", prompt, spicy, intl, images_list=images_list, **fields)

    def flash_reference_to_video(self, prompt, images_list=None, videos_list=None, audios_list=None, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash reference-to-video (up to 10 images, 5 videos, 5 audios)."""
        return self.flash("reference-to-video", prompt, spicy, intl, images_list=images_list,
                          videos_list=videos_list, audios_list=audios_list, **fields)

    def flash_video_edit(self, prompt, video_url, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash video edit (output keeps the source length)."""
        return self.flash("video-edit", prompt, spicy, intl, video_url=video_url, **fields)

    def flash_video_extend(self, prompt, video_url, spicy=False, intl=False, **fields):
        """Seedance 2.5 Flash video extend (``duration`` = seconds to add, 4-30)."""
        return self.flash("video-extend", prompt, spicy, intl, video_url=video_url, **fields)

    # ------------------------------------------------------------------
    # Text-to-video
    # ------------------------------------------------------------------
    def text_to_video(
        self,
        prompt,
        aspect_ratio="16:9",
        duration=5,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Generate a Seedance 2.5 text-to-video clip."""
        return self.generate(
            self._endpoint("text-to-video", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
        )

    def text_to_video_480p(self, prompt, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate a 480p text-to-video clip."""
        return self.text_to_video(prompt, aspect_ratio, duration, seed, variant, "480p")

    def text_to_video_1080p(self, prompt, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 1080p text-to-video clip."""
        return self.text_to_video(prompt, aspect_ratio, duration, seed, variant, "1080p")

    def text_to_video_4k(self, prompt, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 4K text-to-video clip."""
        return self.text_to_video(prompt, aspect_ratio, duration, seed, variant, "4k")

    def intl_text_to_video(self, prompt, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the international Seedance 2.5 text-to-video route."""
        return self.text_to_video(prompt, aspect_ratio, duration, seed, "intl", resolution)

    def spicy_text_to_video(self, prompt, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the Spicy Seedance 2.5 text-to-video route."""
        return self.text_to_video(prompt, aspect_ratio, duration, seed, "spicy", resolution)

    # ------------------------------------------------------------------
    # Image-to-video
    # ------------------------------------------------------------------
    def image_to_video(
        self,
        prompt,
        image_url,
        aspect_ratio="16:9",
        duration=5,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Animate one image into a Seedance 2.5 video clip."""
        return self.generate(
            self._endpoint("image-to-video", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
            image_url=image_url,
        )

    def image_to_video_480p(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate a 480p image-to-video clip."""
        return self.image_to_video(prompt, image_url, aspect_ratio, duration, seed, variant, "480p")

    def image_to_video_1080p(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 1080p image-to-video clip."""
        return self.image_to_video(prompt, image_url, aspect_ratio, duration, seed, variant, "1080p")

    def image_to_video_4k(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 4K image-to-video clip."""
        return self.image_to_video(prompt, image_url, aspect_ratio, duration, seed, variant, "4k")

    def intl_image_to_video(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the international Seedance 2.5 image-to-video route."""
        return self.image_to_video(prompt, image_url, aspect_ratio, duration, seed, "intl", resolution)

    def spicy_image_to_video(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the Spicy Seedance 2.5 image-to-video route."""
        return self.image_to_video(prompt, image_url, aspect_ratio, duration, seed, "spicy", resolution)

    # ------------------------------------------------------------------
    # First & Last Frame
    # ------------------------------------------------------------------
    def first_last_frame(
        self,
        prompt,
        images_list,
        aspect_ratio="16:9",
        duration=5,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Generate a transition between exactly two keyframe images."""
        return self.generate(
            self._endpoint("first-last-frame", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
            images_list=images_list,
        )

    def first_last_frame_480p(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate a 480p First & Last Frame transition."""
        return self.first_last_frame(prompt, images_list, aspect_ratio, duration, seed, variant, "480p")

    def first_last_frame_1080p(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 1080p First & Last Frame transition."""
        return self.first_last_frame(prompt, images_list, aspect_ratio, duration, seed, variant, "1080p")

    def first_last_frame_4k(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None, variant="standard"):
        """Generate an upscaled 4K First & Last Frame transition."""
        return self.first_last_frame(prompt, images_list, aspect_ratio, duration, seed, variant, "4k")

    def intl_first_last_frame(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the international First & Last Frame route."""
        return self.first_last_frame(prompt, images_list, aspect_ratio, duration, seed, "intl", resolution)

    def spicy_first_last_frame(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None, resolution=None):
        """Generate through the Spicy First & Last Frame route."""
        return self.first_last_frame(prompt, images_list, aspect_ratio, duration, seed, "spicy", resolution)

    # ------------------------------------------------------------------
    # Omni Reference
    # ------------------------------------------------------------------
    def omni_reference(
        self,
        prompt,
        aspect_ratio="16:9",
        duration=5,
        images_list=None,
        videos_list=None,
        audios_list=None,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Generate from optional image, video, and audio references."""
        return self.generate(
            self._endpoint("omni-reference", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
            images_list=images_list,
            videos_list=videos_list,
            audios_list=audios_list,
        )

    def omni_reference_480p(self, prompt, aspect_ratio="16:9", duration=5, images_list=None, videos_list=None, audios_list=None, seed=None, variant="standard"):
        """Generate a 480p Omni Reference clip."""
        return self.omni_reference(prompt, aspect_ratio, duration, images_list, videos_list, audios_list, seed, variant, "480p")

    def omni_reference_1080p(self, prompt, aspect_ratio="16:9", duration=5, images_list=None, videos_list=None, audios_list=None, seed=None, variant="standard"):
        """Generate an upscaled 1080p Omni Reference clip."""
        return self.omni_reference(prompt, aspect_ratio, duration, images_list, videos_list, audios_list, seed, variant, "1080p")

    def omni_reference_4k(self, prompt, aspect_ratio="16:9", duration=5, images_list=None, videos_list=None, audios_list=None, seed=None, variant="standard"):
        """Generate an upscaled 4K Omni Reference clip."""
        return self.omni_reference(prompt, aspect_ratio, duration, images_list, videos_list, audios_list, seed, variant, "4k")

    def intl_omni_reference(self, prompt, aspect_ratio="16:9", duration=5, images_list=None, videos_list=None, audios_list=None, seed=None, resolution=None):
        """Generate through the international Omni Reference route."""
        return self.omni_reference(prompt, aspect_ratio, duration, images_list, videos_list, audios_list, seed, "intl", resolution)

    def spicy_omni_reference(self, prompt, aspect_ratio="16:9", duration=5, images_list=None, videos_list=None, audios_list=None, seed=None, resolution=None):
        """Generate through the Spicy Omni Reference route."""
        return self.omni_reference(prompt, aspect_ratio, duration, images_list, videos_list, audios_list, seed, "spicy", resolution)

    # ------------------------------------------------------------------
    # Video edit and extend
    # ------------------------------------------------------------------
    def video_edit(
        self,
        prompt,
        video,
        reference_images=None,
        reference_audios=None,
        aspect_ratio="16:9",
        duration=5,
        generate_audio=True,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Edit an existing video through a Seedance 2.5 Video Edit route."""
        return self.generate(
            self._endpoint("video-edit", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
            video=video,
            reference_images=reference_images,
            reference_audios=reference_audios,
            generate_audio=generate_audio,
        )

    def video_edit_480p(self, prompt, video, reference_images=None, reference_audios=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Edit a video at 480p."""
        return self.video_edit(prompt, video, reference_images, reference_audios, aspect_ratio, duration, generate_audio, seed, variant, "480p")

    def video_edit_1080p(self, prompt, video, reference_images=None, reference_audios=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Edit a video at upscaled 1080p."""
        return self.video_edit(prompt, video, reference_images, reference_audios, aspect_ratio, duration, generate_audio, seed, variant, "1080p")

    def video_edit_4k(self, prompt, video, reference_images=None, reference_audios=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Edit a video at upscaled 4K."""
        return self.video_edit(prompt, video, reference_images, reference_audios, aspect_ratio, duration, generate_audio, seed, variant, "4k")

    def intl_video_edit(self, prompt, video, reference_images=None, reference_audios=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, resolution=None):
        """Edit a video through the international Seedance 2.5 route."""
        return self.video_edit(prompt, video, reference_images, reference_audios, aspect_ratio, duration, generate_audio, seed, "intl", resolution)

    def spicy_video_edit(self, prompt, video, reference_images=None, reference_audios=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, resolution=None):
        """Edit a video through the Spicy Seedance 2.5 route."""
        return self.video_edit(prompt, video, reference_images, reference_audios, aspect_ratio, duration, generate_audio, seed, "spicy", resolution)

    def video_extend(
        self,
        prompt,
        video,
        last_image=None,
        aspect_ratio="16:9",
        duration=5,
        generate_audio=True,
        seed=None,
        variant="standard",
        resolution=None,
    ):
        """Continue an existing video from its final frame."""
        return self.generate(
            self._endpoint("video-extend", variant, resolution),
            prompt,
            aspect_ratio=aspect_ratio,
            duration=duration,
            seed=seed,
            video=video,
            last_image=last_image,
            generate_audio=generate_audio,
        )

    def video_extend_480p(self, prompt, video, last_image=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Continue a video at 480p."""
        return self.video_extend(prompt, video, last_image, aspect_ratio, duration, generate_audio, seed, variant, "480p")

    def video_extend_1080p(self, prompt, video, last_image=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Continue a video at upscaled 1080p."""
        return self.video_extend(prompt, video, last_image, aspect_ratio, duration, generate_audio, seed, variant, "1080p")

    def video_extend_4k(self, prompt, video, last_image=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, variant="standard"):
        """Continue a video at upscaled 4K."""
        return self.video_extend(prompt, video, last_image, aspect_ratio, duration, generate_audio, seed, variant, "4k")

    def intl_video_extend(self, prompt, video, last_image=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, resolution=None):
        """Continue a video through the international Seedance 2.5 route."""
        return self.video_extend(prompt, video, last_image, aspect_ratio, duration, generate_audio, seed, "intl", resolution)

    def spicy_video_extend(self, prompt, video, last_image=None, aspect_ratio="16:9", duration=5, generate_audio=True, seed=None, resolution=None):
        """Continue a video through the Spicy Seedance 2.5 route."""
        return self.video_extend(prompt, video, last_image, aspect_ratio, duration, generate_audio, seed, "spicy", resolution)

    # ------------------------------------------------------------------
    # Character and utility endpoints
    # ------------------------------------------------------------------
    def create_character(self, images_list, outfit_description, character_name=None):
        """Create a reusable character sheet from one to three reference photos."""
        payload = {"images_list": images_list, "prompt": outfit_description}
        if character_name:
            payload["character_name"] = character_name
        return self._post_request("{}/seedance-2-character".format(self.base_url), payload)

    def consistent_video(self, sheet_url, prompt, aspect_ratio="16:9", duration=5, extra_images=None):
        """Anchor an Omni Reference generation on a character sheet image."""
        images_list = [sheet_url]
        if extra_images:
            images_list.extend(extra_images)
        return self.omni_reference(
            prompt=prompt,
            images_list=images_list,
            aspect_ratio=aspect_ratio,
            duration=duration,
        )

    def watermark_remover(self, video_url):
        """Remove a MuAPI watermark from a Seedance video."""
        return self._post_request(
            "{}/seedance-2.0-watermark-remover".format(self.base_url),
            {"video_url": video_url},
        )

    def watermark_remover_pro(self, video_url):
        """Remove a MuAPI watermark with the Pro remover route."""
        return self._post_request(
            "{}/seedance-2-video-watermark-remover-pro".format(self.base_url),
            {"video_url": video_url},
        )

    def legacy_video_edit(self, prompt, video_urls, images_list=None, aspect_ratio="16:9", quality="basic", remove_watermark=False, output_format="mp4"):
        """Call the older Seedance 2.0 video-edit route."""
        payload = {
            "prompt": prompt,
            "video_urls": video_urls,
            "images_list": images_list or [],
            "aspect_ratio": aspect_ratio,
            "quality": quality,
            "remove_watermark": remove_watermark,
            "output_format": output_format,
        }
        return self._post_request("{}/seedance-v2.0-video-edit".format(self.base_url), payload)

    def legacy_extend_video(self, request_id, prompt="", duration=5, quality="basic", output_format="mp4"):
        """Call the older Seedance 2.0 extension route by request ID."""
        payload = {
            "request_id": request_id,
            "prompt": prompt,
            "duration": duration,
            "quality": quality,
            "output_format": output_format,
        }
        return self._post_request("{}/seedance-v2.0-extend".format(self.base_url), payload)

    def upload_file(self, file_path):
        """Upload a local image or video and return its MuAPI URL."""
        endpoint = "{}/upload_file".format(self.base_url)
        with open(file_path, "rb") as file_data:
            response = requests.post(
                endpoint,
                headers={"x-api-key": self.api_key},
                files={"file": file_data},
                timeout=self.upload_timeout,
            )
        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """Read the current status/result for a submitted request."""
        endpoint = "{}/predictions/{}/result".format(self.base_url, request_id)
        response = requests.get(endpoint, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600, max_consecutive_errors=5):
        """
        Poll until a request completes or fails.

        Transient errors while polling (timeouts, dropped connections, HTTP 429
        and 5xx) are retried; polling gives up only after
        ``max_consecutive_errors`` of them in a row. Other HTTP errors, such as
        401 or 404, are raised immediately.
        """
        start_time = time.time()
        consecutive_errors = 0
        while time.time() - start_time < timeout:
            try:
                result = self.get_result(request_id)
            except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as exc:
                if isinstance(exc, requests.HTTPError) and not _is_transient_status(exc.response):
                    raise
                consecutive_errors += 1
                if consecutive_errors >= max_consecutive_errors:
                    raise
                time.sleep(min(poll_interval * 2 ** consecutive_errors, 60))
                continue
            consecutive_errors = 0
            status = result.get("status")
            if status == "completed":
                return result
            if status == "failed":
                raise RuntimeError("Video generation failed: {}".format(result.get("error")))
            time.sleep(poll_interval)
        raise TimeoutError("Timed out waiting for video generation to complete.")

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    try:
        api = SeedanceAPI()
        submission = api.text_to_video(
            prompt="A cinematic shot of a futuristic city with neon lights",
            duration=5,
        )
        request_id = submission.get("request_id")
        print("Task submitted. Request ID: {}".format(request_id))
        result = api.wait_for_completion(request_id)
        print("Generation completed: {}".format(result))
    except Exception as exc:
        print("Error: {}".format(exc))

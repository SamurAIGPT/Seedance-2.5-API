import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SeedanceAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Seedance 2.5 API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")
        
        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, prompt, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 Text-to-Video (T2V) generation task at 720p.

        :param prompt: The text prompt describing the video.
        :param aspect_ratio: Video aspect ratio ('16:9', '9:16', '1:1', '4:3', '3:4', '21:9', '9:21').
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-text-to-video"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 Image-to-Video (I2V) generation task at 720p.

        :param prompt: Text prompt to guide the animation.
        :param image_url: URL of the single image to animate.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-image-to-video"
        payload = {
            "prompt": prompt,
            "image_url": image_url,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def first_last_frame(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 First & Last Frame generation task at 720p.

        Generates a smooth keyframe-driven transition between a start and end image.

        :param prompt: Text prompt describing the desired transition/motion.
        :param images_list: Exactly two image URLs, in order: [first_frame_url, last_frame_url].
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-first-last-frame"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def omni_reference(self, prompt, aspect_ratio="16:9", duration=5,
                        images_list=None, videos_list=None, audios_list=None, seed=None):
        """
        Submits a Seedance 2.5 Omni-Reference generation task at 720p.

        Omni-Reference blends any combination of image, video, and audio references
        into a single guided generation — images steer environment/style, videos steer
        camera motion/rhythm, audio steers mood.

        :param prompt: Text prompt describing the video, referencing the provided assets.
        :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16').
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param images_list: Optional list of up to 20 reference image URLs.
        :param videos_list: Optional list of up to 6 reference video URLs.
        :param audios_list: Optional list of up to 6 reference audio URLs.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-omni-reference"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if images_list:
            payload["images_list"] = images_list
        if videos_list:
            payload["videos_list"] = videos_list
        if audios_list:
            payload["audios_list"] = audios_list
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def create_character(self, images_list, outfit_description, character_name=None):
        """
        Creates a reusable fictional character sheet from reference photos.

        Upload 1–3 images of a real person along with an outfit/style description.
        The API renders a structured character sheet (front, back, side profile, action pose,
        facial expressions, accessories) at 4K / 21:9 and returns a request_id.

        Once completed, pass the sheet URL into consistent_video() to anchor
        an Omni-Reference generation on this character's identity.

        :param images_list: List of 1–3 image URLs of the reference person
                            (clear, well-lit frontal/3/4-angle shots work best).
        :param outfit_description: Description of the desired outfit/style for the character.
        :param character_name: Optional display name for the character.
        :return: JSON response with request_id. Poll wait_for_completion() before use.

        Example workflow::

            # Step 1 — create the character
            char = api.create_character(
                images_list=["https://example.com/person.jpg"],
                outfit_description="cyberpunk jacket with neon accents",
            )
            char_id = char["request_id"]
            sheet_result = api.wait_for_completion(char_id)
            sheet_url = sheet_result["outputs"][0]   # character sheet image URL

            # Step 2 — anchor a generation on the sheet via consistent_video()
            video = api.consistent_video(
                sheet_url=sheet_url,
                prompt="The character rides a motorcycle through a neon-lit city at night",
                aspect_ratio="16:9",
                duration=5,
            )
            result = api.wait_for_completion(video["request_id"])
            print(result["outputs"][0])
        """
        endpoint = f"{self.base_url}/seedance-2-character"
        payload = {
            "images_list": images_list,
            "prompt": outfit_description,
        }
        if character_name:
            payload["character_name"] = character_name
        return self._post_request(endpoint, payload)

    def consistent_video(self, sheet_url, prompt, aspect_ratio="16:9", duration=5, extra_images=None):
        """
        Generate a video with consistent character identity by anchoring on a
        character sheet produced by create_character().

        Uses the Omni-Reference endpoint (not Image-to-Video, which only accepts a
        single image) so the character sheet and any extra scene images can be passed
        together as reference images.

        :param sheet_url: URL of the character sheet image (from wait_for_completion()
                          on a create_character() request — ``result["outputs"][0]``).
        :param prompt: Scene description referencing the character and any extra images.
                       Example: ``"The character from the reference images draws their
                       katana in slow motion, dramatic lighting"``
        :param aspect_ratio: Video aspect ratio (16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 9:21).
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param extra_images: Optional list of additional scene/background image URLs
                             (up to 19 more, since the sheet takes one of the 20 slots).
        :return: JSON response with request_id.

        Example::

            char = api.create_character(
                images_list=["https://example.com/person.jpg"],
                outfit_description="samurai armour with gold trim",
            )
            char_id = char["request_id"]
            sheet_result = api.wait_for_completion(char_id)
            sheet_url = sheet_result["outputs"][0]

            video = api.consistent_video(
                sheet_url=sheet_url,
                prompt="The character from the reference image draws their katana in slow motion, dramatic lighting",
                aspect_ratio="16:9",
                duration=5,
            )
            result = api.wait_for_completion(video["request_id"])
            print(result["outputs"][0])
        """
        images_list = [sheet_url]
        if extra_images:
            images_list.extend(extra_images)

        return self.omni_reference(
            prompt=prompt,
            images_list=images_list,
            aspect_ratio=aspect_ratio,
            duration=duration,
        )

    def extend_video(self, request_id, prompt="", duration=5, quality="basic", output_format="mp4"):
        """
        Extends a previously generated Seedance 2.5 video.

        Note: there is no dedicated Seedance 2.5 extend endpoint yet — this calls the
        Seedance 2.0 video-extend endpoint, which works on any Seedance-family request_id.

        :param request_id: The ID of the video segment to extend.
        :param prompt: Optional text prompt for the extension.
        :param duration: Extension duration in seconds.
        :param output_format: 'mp4' or 'mov'.
        :return: JSON response from the Seedance API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-extend"
        payload = {
            "request_id": request_id,
            "prompt": prompt,
            "duration": duration,
            "quality": quality,
            "output_format": output_format
        }
        return self._post_request(endpoint, payload)

    def video_edit(self, prompt, video_urls, images_list=None, aspect_ratio="16:9", quality="basic", remove_watermark=False,
                    output_format="mp4"):
        """
        Submits a Seedance 2.0 Video-Edit generation task.

        Note: there is no dedicated Seedance 2.5 video-edit endpoint yet — this calls
        the Seedance 2.0 video-edit endpoint.

        :param prompt: The text prompt describing the edit.
        :param video_urls: A list of video URLs to edit.
        :param images_list: Optional list of image URLs.
        :param aspect_ratio: Video aspect ratio.
        :param quality: Output quality.
        :param remove_watermark: Whether to remove watermark.
        :param output_format: 'mp4' (default) or 'mov'.
        :return: JSON response from the Seedance API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-video-edit"
        payload = {
            "prompt": prompt,
            "video_urls": video_urls,
            "images_list": images_list or [],
            "aspect_ratio": aspect_ratio,
            "quality": quality,
            "remove_watermark": remove_watermark,
            "output_format": output_format
        }
        return self._post_request(endpoint, payload)

    def watermark_remover(self, video_url):
        """
        Removes watermark from a Seedance video.
        
        :param video_url: URL of the video to process.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.0-watermark-remover"
        payload = {
            "video_url": video_url
        }
        return self._post_request(endpoint, payload)

    def watermark_remover_pro(self, video_url):
        """
        Removes watermark from a Seedance video (Pro version).
        
        :param video_url: URL of the video to process.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2-video-watermark-remover-pro"
        payload = {
            "video_url": video_url
        }
        return self._post_request(endpoint, payload)

    def text_to_video_480p(self, prompt, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 Text-to-Video (T2V) 480p task — faster/cheaper than the 720p tier.

        :param prompt: Descriptive text prompt.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-text-to-video-480p"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def image_to_video_480p(self, prompt, image_url, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 Image-to-Video (I2V) 480p task — faster/cheaper than the 720p tier.

        :param prompt: Text prompt to guide the animation.
        :param image_url: URL of the single image to animate.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-image-to-video-480p"
        payload = {
            "prompt": prompt,
            "image_url": image_url,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def first_last_frame_480p(self, prompt, images_list, aspect_ratio="16:9", duration=5, seed=None):
        """
        Submits a Seedance 2.5 First & Last Frame 480p task — faster/cheaper than the 720p tier.

        :param prompt: Text prompt describing the desired transition/motion.
        :param images_list: Exactly two image URLs, in order: [first_frame_url, last_frame_url].
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.5-first-last-frame-480p"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def omni_reference_480p(self, prompt, aspect_ratio="16:9", duration=5,
                             images_list=None, videos_list=None, audios_list=None, seed=None):
        """
        Submits a Seedance 2.5 Omni-Reference 480p task — faster/cheaper than the 720p tier.

        :param prompt: Text prompt describing the video, referencing the provided assets.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration in seconds, 4-30. Default 5.
        :param images_list: Optional list of up to 20 reference image URLs.
        :param videos_list: Optional list of up to 6 reference video URLs.
        :param audios_list: Optional list of up to 6 reference audio URLs.
        :param seed: Optional int seed (-1 to 4294967295) for reproducible generation.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-omni-reference-480p"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        if images_list:
            payload["images_list"] = images_list
        if videos_list:
            payload["videos_list"] = videos_list
        if audios_list:
            payload["audios_list"] = audios_list
        if seed is not None:
            payload["seed"] = seed
        return self._post_request(endpoint, payload)

    def vip_text_to_video_1080p(self, prompt, aspect_ratio="16:9", duration=5):
        """
        Submits a Seedance 2 VIP Text-to-Video 1080p task (coming soon).

        VIP tier — priority queue, low censorship, full 1080p output.

        :param prompt: Text description of the video to generate.
        :param aspect_ratio: Output aspect ratio (e.g. '16:9', '9:16', '1:1').
        :param duration: Video duration in seconds (4–15).
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/sd-2-vip-text-to-video-1080p"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        return self._post_request(endpoint, payload)

    def vip_text_to_video_fast_1080p(self, prompt, aspect_ratio="16:9", duration=5):
        """
        Submits a Seedance 2 VIP Text-to-Video 1080p Fast task (coming soon).

        VIP fast tier — fastest 1080p text-to-video with priority queue and low censorship.

        :param prompt: Text description of the video to generate.
        :param aspect_ratio: Output aspect ratio (e.g. '16:9', '9:16', '1:1').
        :param duration: Video duration in seconds (4–15).
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/sd-2-vip-text-to-video-fast-1080p"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        return self._post_request(endpoint, payload)

    def vip_image_to_video_1080p(self, prompt, images_list, aspect_ratio="16:9", duration=5):
        """
        Submits a Seedance 2 VIP Image-to-Video 1080p task (coming soon).

        VIP tier — priority queue, low censorship, full 1080p output.

        :param prompt: Optional text prompt guiding the motion.
        :param images_list: List containing the start-frame image URL.
        :param aspect_ratio: Output aspect ratio (e.g. '16:9', '9:16', '1:1').
        :param duration: Video duration in seconds (4–15).
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/sd-2-vip-image-to-video-1080p"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        return self._post_request(endpoint, payload)

    def vip_image_to_video_fast_1080p(self, prompt, images_list, aspect_ratio="16:9", duration=5):
        """
        Submits a Seedance 2 VIP Image-to-Video 1080p Fast task (coming soon).

        VIP fast tier — fastest 1080p image animation with priority queue and low censorship.

        :param prompt: Optional text prompt guiding the motion.
        :param images_list: List containing the start-frame image URL.
        :param aspect_ratio: Output aspect ratio (e.g. '16:9', '9:16', '1:1').
        :param duration: Video duration in seconds (4–15).
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/sd-2-vip-image-to-video-fast-1080p"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
        }
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image or video) to MuAPI for use in generation tasks.
        
        :param file_path: Path to the local file to upload.
        :return: JSON response from the MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"
        
        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }
        
        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)
            
        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600):
        """
        Waits for the video generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")
            
            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Video generation failed: {result.get('error')}")
            
            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)
        
        raise TimeoutError("Timed out waiting for video generation to complete.")

if __name__ == "__main__":
    # Example usage for T2V
    try:
        api = SeedanceAPI()
        prompt = "A cinematic shot of a futuristic city with neon lights, 8k resolution"
        
        print(f"Submitting T2V task with prompt: {prompt}")
        submission = api.text_to_video(prompt=prompt, duration=5)
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")
        
        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Video URL: {result.get('url')}")
        
    except Exception as e:
        print(f"Error: {e}")

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

    def text_to_video(self, prompt, aspect_ratio="16:9", duration=5, quality="basic", remove_watermark=False):
        """
        Submits a Seedance 2.5 Text-to-Video (T2V) generation task.

        :param prompt: The text prompt describing the video. To use a fictional character,
                       reference it inline with @character:<id> where <id> is the request_id
                       from a completed create_character() call. Multiple characters supported.
                       Example: "@character:ab539e5f-... walks on the beach at sunset"
        :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16').
        :param duration: Video duration in seconds.
        :param quality: Output quality ('basic' or 'high').
        :param remove_watermark: Whether to remove the watermark.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-t2v"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality,
            "remove_watermark": remove_watermark
        }
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, images_list, aspect_ratio="16:9", duration=5, quality="basic", remove_watermark=False):
        """
        Submits a Seedance 2.5 Image-to-Video (I2V) generation task.

        :param prompt: Text prompt to guide the animation. Reference images in the list with
                       @image1, @image2, etc. To inject a character from create_character(),
                       use @character:<id> inline — e.g. "@image1 shows the scene, @character:ab539e5f-... is the hero".
                       Characters are appended after images_list entries automatically.
        :param images_list: A list of image URLs to animate.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration.
        :param quality: Output quality.
        :param remove_watermark: Whether to remove the watermark.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-i2v"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality,
            "remove_watermark": remove_watermark
        }
        return self._post_request(endpoint, payload)

    def omni_reference(self, prompt, aspect_ratio="16:9", duration=5, quality="basic",
                        images_list=None, video_files=None, audio_files=None):
        """
        Submits a Seedance 2.5 Omni-Reference generation task.

        Omni-Reference lets you condition a video on any combination of image, video,
        and audio references — all in a single request. Use @character:<id> inline in
        the prompt to inject a fictional character created via create_character().

        :param prompt: Text prompt describing the video. Supports @character:<id> syntax.
        :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16').
        :param duration: Video duration in seconds (minimum 4 s for video references).
        :param quality: Output quality ('basic' or 'high').
        :param images_list: Optional list of image URLs to condition on.
        :param video_files: Optional list of video URLs to condition on.
        :param audio_files: Optional list of audio URLs to condition on.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.0-omni-reference"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality,
        }
        if images_list:
            payload["images_list"] = images_list
        if video_files:
            payload["video_files"] = video_files
        if audio_files:
            payload["audio_files"] = audio_files
        return self._post_request(endpoint, payload)

    def create_character(self, images_list, outfit_description, character_name=None):
        """
        Creates a reusable fictional character sheet from reference photos.

        Upload 1–3 images of a real person along with an outfit/style description.
        The API renders a structured character sheet (front, back, side profile, action pose,
        facial expressions, accessories) at 4K / 21:9 and returns a request_id.

        Once completed the character can be:
          - Referenced inline in any T2V, I2V, or Omni-Reference prompt using
            ``@character:<request_id>``
          - Used directly as the anchor image in consistent_video() for tighter
            face/identity preservation

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

            # Step 2a — use @character:<id> inline in T2V
            video = api.text_to_video(
                prompt=f"@character:{char_id} rides a motorcycle through a neon-lit city",
                aspect_ratio="16:9",
                duration=5,
            )

            # Step 2b — OR use consistent_video() for direct sheet-anchored I2V
            video = api.consistent_video(
                sheet_url=sheet_url,
                prompt="@image1 rides a motorcycle through a neon-lit city at night",
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

    def consistent_video(self, sheet_url, prompt, aspect_ratio="16:9", duration=5,
                         quality="basic", extra_images=None):
        """
        Generate a video with consistent character identity by anchoring on a
        character sheet produced by create_character().

        The sheet is passed as the first reference image (``@image1``) in an
        Image-to-Video request. Use ``@image1`` in the prompt to refer to the
        character — it is automatically prepended if omitted.

        :param sheet_url: URL of the character sheet image (from wait_for_completion()
                          on a create_character() request — ``result["outputs"][0]``).
        :param prompt: Scene description. Use ``@image1`` to address the character,
                       ``@image2``/``@image3`` for any extra scene images.
                       Example: ``"@image1 walks through a neon-lit city at night"``
        :param aspect_ratio: Video aspect ratio (16:9 / 9:16 / 4:3 / 3:4).
        :param duration: 5 / 10 / 15 seconds.
        :param quality: ``"basic"`` or ``"high"`` (2K).
        :param extra_images: Optional list of additional scene/background image URLs
                             (referenced as @image2, @image3 in the prompt).
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
                prompt="@image1 draws their katana in slow motion, dramatic lighting",
                aspect_ratio="16:9",
                duration=5,
                quality="high",
            )
            result = api.wait_for_completion(video["request_id"])
            print(result["outputs"][0])
        """
        images_list = [sheet_url]
        if extra_images:
            images_list.extend(extra_images)

        # Ensure the prompt references @image1 so the model anchors on the sheet
        if "@image1" not in prompt:
            prompt = f"@image1 {prompt.strip()}"

        return self.image_to_video(
            prompt=prompt,
            images_list=images_list,
            aspect_ratio=aspect_ratio,
            duration=duration,
            quality=quality,
        )

    def extend_video(self, request_id, prompt="", duration=5, quality="basic"):
        """
        Extends a previously generated Seedance 2.5 video.
        
        :param request_id: The ID of the video segment to extend.
        :param prompt: Optional text prompt for the extension.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-extend"
        payload = {
            "request_id": request_id,
            "prompt": prompt,
            "duration": duration,
            "quality": quality
        }
        return self._post_request(endpoint, payload)

    def video_edit(self, prompt, video_urls, images_list=None, aspect_ratio="16:9", quality="basic", remove_watermark=False):
        """
        Submits a Seedance 2.5 Video-Edit generation task.
        
        :param prompt: The text prompt describing the edit.
        :param video_urls: A list of video URLs to edit.
        :param images_list: Optional list of image URLs.
        :param aspect_ratio: Video aspect ratio.
        :param quality: Output quality.
        :param remove_watermark: Whether to remove watermark.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-v2.0-video-edit"
        payload = {
            "prompt": prompt,
            "video_urls": video_urls,
            "images_list": images_list or [],
            "aspect_ratio": aspect_ratio,
            "quality": quality,
            "remove_watermark": remove_watermark
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

    def text_to_video_480p(self, prompt, aspect_ratio="16:9", duration=5, quality="basic"):
        """
        Submits a Seedance 2.5 Text-to-Video (T2V) 480p task.
        
        :param prompt: Descriptive text prompt.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration.
        :param quality: Output quality.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.0-t2v-480p"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality
        }
        return self._post_request(endpoint, payload)

    def image_to_video_480p(self, prompt, images_list, aspect_ratio="16:9", duration=5, quality="basic"):
        """
        Submits a Seedance 2.5 Image-to-Video (I2V) 480p task.
        
        :param prompt: Text prompt to guide the animation.
        :param images_list: List of image URLs.
        :param aspect_ratio: Video aspect ratio.
        :param duration: Video duration.
        :param quality: Output quality.
        :return: JSON response from the Seedance 2.5 API.
        """
        endpoint = f"{self.base_url}/seedance-2.0-i2v-480p"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "quality": quality
        }
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

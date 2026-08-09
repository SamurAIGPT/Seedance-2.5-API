import json
from typing import List, Optional

from mcp.server.fastmcp import FastMCP

from seedance_api import SEEDANCE_25_ENDPOINTS, SeedanceAPI


mcp = FastMCP("Seedance 2.5 API Server")


def get_api():
    return SeedanceAPI()


@mcp.tool()
def generate_seedance_25(
    endpoint: str,
    prompt: str,
    aspect_ratio: str = "16:9",
    duration: int = 5,
    seed: Optional[int] = None,
    image_url: Optional[str] = None,
    images_list: Optional[List[str]] = None,
    videos_list: Optional[List[str]] = None,
    audios_list: Optional[List[str]] = None,
    video: Optional[str] = None,
    reference_images: Optional[List[str]] = None,
    reference_audios: Optional[List[str]] = None,
    last_image: Optional[str] = None,
    generate_audio: Optional[bool] = None,
    webhook_url: Optional[str] = None,
) -> str:
    """
    Submit any current Seedance 2.5 request.

    ``endpoint`` accepts the full MuAPI route slug, including standard,
    intl, and spicy 480p/720p/1080p/4k variants. Use image_url for I2V,
    exactly two images_list entries for First & Last Frame, the three
    reference lists for Omni Reference, and video plus the edit/extend
    fields for Video Edit or Video Extend.
    """
    if endpoint not in SEEDANCE_25_ENDPOINTS:
        raise ValueError("Unsupported Seedance 2.5 endpoint: {}".format(endpoint))
    result = get_api().generate(
        endpoint=endpoint,
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        duration=duration,
        seed=seed,
        image_url=image_url,
        images_list=images_list,
        videos_list=videos_list,
        audios_list=audios_list,
        video=video,
        reference_images=reference_images,
        reference_audios=reference_audios,
        last_image=last_image,
        generate_audio=generate_audio,
        webhook_url=webhook_url,
    )
    return json.dumps(result, indent=2)


@mcp.tool()
def text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, seed: Optional[int] = None) -> str:
    """Generate a standard 720p video from text."""
    return json.dumps(get_api().text_to_video(prompt, aspect_ratio, duration, seed), indent=2)


@mcp.tool()
def image_to_video(prompt: str, image_url: str, aspect_ratio: str = "16:9", duration: int = 5, seed: Optional[int] = None) -> str:
    """Animate one image into a standard 720p video."""
    return json.dumps(get_api().image_to_video(prompt, image_url, aspect_ratio, duration, seed), indent=2)


@mcp.tool()
def first_last_frame(prompt: str, images_list: List[str], aspect_ratio: str = "16:9", duration: int = 5, seed: Optional[int] = None) -> str:
    """Generate a standard 720p transition between two images."""
    return json.dumps(get_api().first_last_frame(prompt, images_list, aspect_ratio, duration, seed), indent=2)


@mcp.tool()
def omni_reference(
    prompt: str,
    aspect_ratio: str = "16:9",
    duration: int = 5,
    images_list: Optional[List[str]] = None,
    videos_list: Optional[List[str]] = None,
    audios_list: Optional[List[str]] = None,
    seed: Optional[int] = None,
) -> str:
    """Generate a standard 720p video from multimodal references."""
    result = get_api().omni_reference(
        prompt,
        aspect_ratio,
        duration,
        images_list,
        videos_list,
        audios_list,
        seed,
    )
    return json.dumps(result, indent=2)


@mcp.tool()
def video_edit(
    prompt: str,
    video: str,
    reference_images: Optional[List[str]] = None,
    reference_audios: Optional[List[str]] = None,
    aspect_ratio: str = "16:9",
    duration: int = 5,
    generate_audio: bool = True,
    seed: Optional[int] = None,
) -> str:
    """Edit an existing video through the standard 720p route."""
    result = get_api().video_edit(
        prompt,
        video,
        reference_images,
        reference_audios,
        aspect_ratio,
        duration,
        generate_audio,
        seed,
    )
    return json.dumps(result, indent=2)


@mcp.tool()
def video_extend(
    prompt: str,
    video: str,
    last_image: Optional[str] = None,
    aspect_ratio: str = "16:9",
    duration: int = 5,
    generate_audio: bool = True,
    seed: Optional[int] = None,
) -> str:
    """Continue an existing video through the standard 720p route."""
    result = get_api().video_extend(
        prompt,
        video,
        last_image,
        aspect_ratio,
        duration,
        generate_audio,
        seed,
    )
    return json.dumps(result, indent=2)


@mcp.tool()
def spicy_text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, seed: Optional[int] = None) -> str:
    """Generate a standard-resolution Spicy text-to-video clip."""
    return json.dumps(get_api().spicy_text_to_video(prompt, aspect_ratio, duration, seed), indent=2)


@mcp.tool()
def spicy_image_to_video(prompt: str, image_url: str, aspect_ratio: str = "16:9", duration: int = 5, seed: Optional[int] = None) -> str:
    """Generate a standard-resolution Spicy image-to-video clip."""
    return json.dumps(get_api().spicy_image_to_video(prompt, image_url, aspect_ratio, duration, seed), indent=2)


@mcp.tool()
def create_character(images_list: List[str], outfit_description: str, character_name: Optional[str] = None) -> str:
    """Create a reusable character sheet from reference photos."""
    return json.dumps(get_api().create_character(images_list, outfit_description, character_name), indent=2)


@mcp.tool()
def watermark_remover(video_url: str) -> str:
    """Remove a MuAPI watermark from a Seedance video."""
    return json.dumps(get_api().watermark_remover(video_url), indent=2)


@mcp.tool()
def watermark_remover_pro(video_url: str) -> str:
    """Remove a MuAPI watermark with the Pro remover route."""
    return json.dumps(get_api().watermark_remover_pro(video_url), indent=2)


@mcp.tool()
def upload_file(file_path: str) -> str:
    """Upload a local image or video for use in a generation request."""
    return json.dumps(get_api().upload_file(file_path), indent=2)


@mcp.tool()
def get_task_status(request_id: str) -> str:
    """Check the status and output of a generation task."""
    return json.dumps(get_api().get_result(request_id), indent=2)


if __name__ == "__main__":
    mcp.run()

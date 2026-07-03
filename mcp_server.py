import os
import json
from mcp.server.fastmcp import FastMCP
from seedance_api import SeedanceAPI

# Initialize FastMCP server
mcp = FastMCP("Seedance 2.5 API Server")

# Helper to get API client
def get_api():
    return SeedanceAPI()

@mcp.tool()
def text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, quality: str = "basic", remove_watermark: bool = False) -> str:
    """
    Generate a video from a text prompt using Seedance 2.5.
    
    :param prompt: Descriptive text prompt. Use @character:<id> for consistent characters.
    :param aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16', '1:1').
    :param duration: Duration in seconds (5 or 10).
    :param quality: 'basic' or 'high'.
    :param remove_watermark: Whether to remove the MuAPI watermark.
    """
    api = get_api()
    result = api.text_to_video(prompt, aspect_ratio, duration, quality, remove_watermark)
    return json.dumps(result, indent=2)

@mcp.tool()
def image_to_video(prompt: str, images_list: list[str], aspect_ratio: str = "16:9", duration: int = 5, quality: str = "basic", remove_watermark: bool = False) -> str:
    """
    Animate static images into a video using Seedance 2.5.
    
    :param prompt: Text prompt guiding the animation.
    :param images_list: List of image URLs to animate.
    :param aspect_ratio: Video aspect ratio.
    :param duration: Duration in seconds.
    :param quality: 'basic' or 'high'.
    :param remove_watermark: Whether to remove the MuAPI watermark.
    """
    api = get_api()
    result = api.image_to_video(prompt, images_list, aspect_ratio, duration, quality, remove_watermark)
    return json.dumps(result, indent=2)

@mcp.tool()
def omni_reference(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, quality: str = "basic", 
                   images_list: list[str] = None, video_files: list[str] = None, audio_files: list[str] = None) -> str:
    """
    Generate a video conditioned on a mix of image, video, and audio references.
    
    :param prompt: Descriptive prompt.
    :param aspect_ratio: Video aspect ratio.
    :param duration: Duration in seconds.
    :param quality: 'basic' or 'high'.
    :param images_list: Optional image URLs.
    :param video_files: Optional video URLs.
    :param audio_files: Optional audio URLs.
    """
    api = get_api()
    result = api.omni_reference(prompt, aspect_ratio, duration, quality, images_list, video_files, audio_files)
    return json.dumps(result, indent=2)

@mcp.tool()
def create_character(images_list: list[str], outfit_description: str, character_name: str = None) -> str:
    """
    Create a consistent character sheet from reference photos.
    Returns a request_id for a character sheet image.
    
    :param images_list: 1-3 image URLs of a real person.
    :param outfit_description: Style/outfit description for the character.
    :param character_name: Optional name for the character.
    """
    api = get_api()
    result = api.create_character(images_list, outfit_description, character_name)
    return json.dumps(result, indent=2)

@mcp.tool()
def extend_video(request_id: str, prompt: str = "", duration: int = 5, quality: str = "basic") -> str:
    """
    Extend a previously generated Seedance 2.5 video segment.
    
    :param request_id: ID of the video to extend.
    :param prompt: Optional prompt for the extension.
    :param duration: Seconds to extend (e.g., 5).
    :param quality: 'basic' or 'high'.
    """
    api = get_api()
    result = api.extend_video(request_id, prompt, duration, quality)
    return json.dumps(result, indent=2)

@mcp.tool()
def video_edit(prompt: str, video_urls: list[str], images_list: list[str] = None, 
               aspect_ratio: str = "16:9", quality: str = "basic", remove_watermark: bool = False) -> str:
    """
    Edit an existing video or apply styles using natural language.
    
    :param prompt: Describe the desired edits.
    :param video_urls: List of video URLs to edit.
    :param images_list: Optional reference image URLs.
    :param aspect_ratio: Video aspect ratio.
    :param quality: 'basic' or 'high'.
    :param remove_watermark: Whether to remove the watermark.
    """
    api = get_api()
    result = api.video_edit(prompt, video_urls, images_list, aspect_ratio, quality, remove_watermark)
    return json.dumps(result, indent=2)

@mcp.tool()
def watermark_remover(video_url: str) -> str:
    """
    Remove MuAPI watermark from a Seedance video.
    """
    api = get_api()
    result = api.watermark_remover(video_url)
    return json.dumps(result, indent=2)

@mcp.tool()
def watermark_remover_pro(video_url: str) -> str:
    """
    Remove MuAPI watermark from a Seedance video (Pro version).
    """
    api = get_api()
    result = api.watermark_remover_pro(video_url)
    return json.dumps(result, indent=2)

@mcp.tool()
def t2v_480p(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, quality: str = "basic") -> str:
    """
    Generate a 480p video from text (faster/cheaper).
    """
    api = get_api()
    result = api.text_to_video_480p(prompt, aspect_ratio, duration, quality)
    return json.dumps(result, indent=2)

@mcp.tool()
def i2v_480p(prompt: str, images_list: list[str], aspect_ratio: str = "16:9", duration: int = 5, quality: str = "basic") -> str:
    """
    Generate a 480p video from an image (faster/cheaper).
    """
    api = get_api()
    result = api.image_to_video_480p(prompt, images_list, aspect_ratio, duration, quality)
    return json.dumps(result, indent=2)

@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image or video) to MuAPI for use in generation tasks.
    
    :param file_path: Local path to the file.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.
    
    :param request_id: The ID returned from a generation tool call.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run()

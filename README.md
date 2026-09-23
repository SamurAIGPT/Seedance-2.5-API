# Seedance 2.5 API: Python Wrapper for ByteDance's AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedance-2-5-api)

[![PyPI version](https://img.shields.io/pypi/v/seedance-2-api.svg)](https://pypi.org/project/seedance-2-api/)
[![GitHub stars](https://img.shields.io/github/stars/SamurAIGPT/Seedance-2.5-API.svg)](https://github.com/SamurAIGPT/Seedance-2.5-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2.5 API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api). Generate cinematic, high-fidelity AI videos from text prompts and static images — with industry-leading **realistic human face generation** — using ByteDance's most advanced video generation model.

Join the subreddit https://www.reddit.com/r/Seedance_2_API/ for discussions on using the Seedance 2.5 API.

> 🌟 **Seedance 2.5** now exposes 72 early-access routes across Text-to-Video, Image-to-Video, First & Last Frame, Omni Reference, Video Edit, and Video Extend. Every workflow is available in standard, Intl, and Spicy variants with 480p, 720p, upscaled 1080p, and upscaled 4K tiers. Clips support 4–30 seconds; Omni Reference accepts up to 30 images, 10 videos, and 10 audio files. Try it now: [I2V Playground](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [T2V Playground](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## 📺 Video Tutorial

[![How to Access Seedance 2.5 API (Step-by-Step Guide)](https://img.youtube.com/vi/Uszlw7H4VP4/maxresdefault.jpg)](https://www.youtube.com/watch?v=Uszlw7H4VP4)

**[How to Access Seedance 2.5 API (Step-by-Step Guide)](https://www.youtube.com/watch?v=Uszlw7H4VP4)** — a full walkthrough of getting an API key and making your first Seedance 2.5 call via [MuAPI](https://muapi.ai/seedance-2.5?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api).

## Related Projects

- [seedance-2.0-watermark-remover](https://github.com/SamurAIGPT/seedance-2.0-watermark-remover) — Remove watermarks from your Seedance generated videos
- [seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) — Ready-made Next.js SaaS built on Seedance 2
- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper covering Seedance 2.0 and Seedance 2 Mini
- [Seedance-3-API](https://github.com/Anil-matcha/Seedance-3-API) — companion project for the next Seedance API generation on MuAPI
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide, prompts, camera controls, and video generation examples
- [seedance2.5-comfyui](https://github.com/Anil-matcha/seedance2.5-comfyui) — Native Seedance 2.5 ComfyUI custom nodes and example workflows
- [seedance-2.5-mcp](https://github.com/Anil-matcha/seedance-2.5-mcp) — Focused MCP server for the standard 720p and 480p Seedance 2.5 Preview routes
- [seedance-2-mcp](https://github.com/Anil-matcha/seedance-2-mcp) — Focused MCP server for the related Seedance 2 workflows
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper for Black Forest Labs' FLUX 3 Text-to-Video and Image-to-Video

## 🚀 Why Use Seedance 2.5 API?

Seedance 2.5 is ByteDance's most advanced video generation model, offering unparalleled video quality and motion consistency.

- **Longer Clips**: Generate up to 30 seconds per clip (up from 15s on Seedance 2.0).
- **Realistic Human Faces**: Best-in-class facial fidelity — natural expressions, skin detail, and identity consistency across frames.
- **Less Censorship**: More permissive content policy compared to other AI video models, enabling a wider range of creative use cases.
- **Superior Motion Control**: Advanced camera movement and improved character consistency for professional results.
- **Multimodal API**: Supports Text-to-Video (T2V), Image-to-Video (I2V), First & Last Frame keyframe transitions, Omni Reference, Video Edit, and Video Extend.
- **Developer-First**: Fast processing via the MuAPI infrastructure with a simple Python SDK.

## 🌟 Key Features of Seedance 2.5 API

- ✅ **Realistic Human Face Generation**: Produces natural, high-fidelity human faces with accurate expressions, skin texture, and identity consistency — no uncanny valley.
- ✅ **Seedance 2.5 Text-to-Video (T2V)**: Transform complex descriptive prompts into stunning AI video clips, up to 30s long.
- ✅ **Seedance 2.5 Image-to-Video (I2V)**: Animate a single static image with precise motion control using `image_url`.
- ✅ **Seedance 2.5 First & Last Frame**: Generate a smooth keyframe-driven transition between a start and end image.
- ✅ **Seedance 2.5 Omni Reference**: Condition a video on any combination of image, video, and audio references in one request — up to 30 reference images, 10 reference videos, and 10 reference audio clips.
- ✅ **Seedance Character**: Generate a multi-panel character sheet (front, back, side, action pose, expressions) from 1–3 reference photos, then anchor an Omni-Reference generation on it via `consistent_video()` for consistent identity across shots.
- ✅ **Resolution Tiers**: Choose 480p for fast drafts, 720p for the standard tier, or upscaled 1080p and 4K routes for higher-resolution deliverables.
- ✅ **Intl and Spicy Variants**: Select the international or relaxed-content-safety route family without changing the request shape.
- ✅ **Video Edit and Extend**: Edit an input video with reference images/audio or continue it from its last frame, with optional synchronized audio generation.
- ✅ **Reproducible Seeds**: Pass `seed` to keep generations in the same neighborhood across repeated calls.
- ✅ **File Upload**: Directly upload local images and videos using the `upload_file` method, supporting seamless use in generation tasks.
- ✅ **Less Censorship**: More permissive content policy than competing models — broader creative freedom out of the box.
- ✅ **Flexible Aspect Ratios**: `16:9`, `9:16` (TikTok/Reels), `1:1`, `4:3`, `3:4`, `21:9`, `9:21`.

> **Resolution note**: The 1080p and 4K routes are upscaled from the model's 720p base render. They are separate routes and are priced above the standard 720p tier.
> **Access note**: Seedance 2.5 is an early-access build on MuAPI, gated to Pro/Business plan accounts.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install seedance-2-api
```

### From Source
```bash
# Clone the Seedance 2.5 API repository
git clone https://github.com/SamurAIGPT/Seedance-2.5-API.git
cd Seedance-2.5-API

# Install required dependencies
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 Seedance 2.5 MCP Server (New!)

You can now use Seedance 2.5 as an **MCP (Model Context Protocol)** server. This allows AI models (like Claude Desktop or Cursor) to directly invoke Seedance tools.

The `generate_seedance_25` tool accepts the exact endpoint slug from the route
matrix, so MCP clients can select any standard, Intl, or Spicy workflow and
resolution tier without waiting for a new tool wrapper.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start with Seedance 2.5 API (Python)

```python
from seedance_api import SeedanceAPI

# Initialize the Seedance 2.5 client
api = SeedanceAPI()

# 1. Generate Video from Text (T2V) using Seedance 2.5 API
print("Generating AI Video using Seedance 2.5...")
submission = api.text_to_video(
    prompt="A cinematic slow-motion shot of a cyberpunk city in the rain, neon lights reflecting on puddles, 8k resolution",
    aspect_ratio="16:9",
    duration=5,
)

# 2. Wait for completion
result = api.wait_for_completion(submission['request_id'])
video_url = result.get("output", {}).get("video") or result.get("url")
print(f"Success! View your Seedance 2.5 video here: {video_url}")
```

---

## 📡 API Endpoints & Reference

The base URL is `https://api.muapi.ai/api/v1`. MuAPI exposes 72 Seedance 2.5
routes: six workflows × three variants × four resolution tiers. Every route
returns a `request_id` that can be polled with the result endpoint below.

### Route matrix

The route names below are the 720p bases. Append `-480p`, `-1080p`, or `-4k`
to select another tier; the unsuffixed route is 720p. The 1080p and 4K routes
are upscaled from the 720p base render.

| Variant | Text-to-Video | Image-to-Video | First & Last Frame | Omni Reference | Video Edit | Video Extend |
|---|---|---|---|---|---|---|
| Standard | `seedance-2.5-text-to-video` | `seedance-2.5-image-to-video` | `seedance-2.5-first-last-frame` | `seedance-2.5-omni-reference` | `seedance-2.5-video-edit` | `seedance-2.5-video-extend` |
| Intl | `seedance-2.5-intl-text-to-video` | `seedance-2.5-intl-image-to-video` | `seedance-2.5-intl-first-last-frame` | `seedance-2.5-intl-omni-reference` | `seedance-2.5-intl-video-edit` | `seedance-2.5-intl-video-extend` |
| Spicy | `seedance-2.5-spicy-text-to-video` | `seedance-2.5-spicy-image-to-video` | `seedance-2.5-spicy-first-last-frame` | `seedance-2.5-spicy-omni-reference` | `seedance-2.5-spicy-video-edit` | `seedance-2.5-spicy-video-extend` |

Standard and Intl pricing is `$0.17/sec` at 480p, `$0.34/sec` at 720p,
`$0.85/sec` at 1080p, and `$1.70/sec` at 4K for T2V/I2V/keyframe/Omni
routes. Video Edit and Video Extend start at `$0.1105/sec`, `$0.221/sec`,
`$0.5525/sec`, and `$1.105/sec` respectively because the input video is
priced with the reference-video rate. Spicy routes use the same shapes and
are priced 10% above the matching standard tier.

### Text-to-Video and Image-to-Video

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-text-to-video-1080p" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas",
      "aspect_ratio": "16:9",
      "duration": 5,
      "seed": 42
  }'
```

Image-to-Video uses one `image_url` (not a list):

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-intl-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The camera slowly pushes in as the subject turns toward the light",
      "image_url": "https://example.com/photo.jpg",
      "aspect_ratio": "16:9",
      "duration": 8
  }'
```

### First & Last Frame

Pass exactly two URLs in `images_list`, in start/end order:

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-spicy-first-last-frame-480p" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Smooth cinematic transition as the scene shifts from day to night",
      "images_list": ["https://example.com/start.jpg", "https://example.com/end.jpg"],
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### Omni Reference

Omni Reference accepts up to 30 images, 10 video clips, and 10 audio files:

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-omni-reference-4k" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A dramatic chase through a neon city, matching the reference style and camera rhythm",
      "aspect_ratio": "16:9",
      "duration": 5,
      "images_list": ["https://example.com/scene.jpg"],
      "videos_list": ["https://example.com/motion.mp4"],
      "audios_list": ["https://example.com/mood.mp3"]
  }'
```

### Video Edit

Video Edit takes a single source `video`, optional `reference_images` and
`reference_audios`, and a `generate_audio` flag:

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-video-edit-1080p" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Turn the sunny afternoon into a rainy blue-hour scene while preserving the subject and camera movement",
      "video": "https://example.com/input.mp4",
      "reference_images": ["https://example.com/style.jpg"],
      "generate_audio": true,
      "duration": 8,
      "aspect_ratio": "16:9"
  }'
```

### Video Extend

Video Extend continues from the source video's final frame. Set `last_image`
when the continuation should interpolate toward a target frame:

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-intl-video-extend-4k" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Continue the camera move forward into the glowing city entrance",
      "video": "https://example.com/input.mp4",
      "last_image": "https://example.com/target.jpg",
      "duration": 5,
      "generate_audio": true
  }'
```

### Polling for Results

```python
import time
import requests


def wait_for_result(request_id, api_key, poll_interval=5, timeout=600):
    start = time.time()
    while time.time() - start < timeout:
        result = requests.get(
            "https://api.muapi.ai/api/v1/predictions/{}/result".format(request_id),
            headers={"x-api-key": api_key},
        ).json()
        if result["status"] == "completed":
            return result
        if result["status"] == "failed":
            raise RuntimeError(result.get("error", "Generation failed"))
        time.sleep(poll_interval)
    raise TimeoutError("Generation timed out")
```

### MuAPI Parameters

| Parameter | Type | Applies to | Description |
|---|---|---|---|
| `prompt` | string | All routes | Required scene, motion, edit, or continuation instructions |
| `image_url` | URL | Image-to-Video | One input image |
| `images_list` | URL array | First & Last / Omni | Exactly 2 keyframes, or up to 30 Omni references |
| `videos_list` | URL array | Omni Reference | Up to 10 reference clips |
| `audios_list` | URL array | Omni Reference | Up to 10 reference audio files |
| `video` | URL | Video Edit / Extend | Source video; clips longer than 30s are trimmed |
| `reference_images` | URL array | Video Edit | Optional identity/style references, up to 30 |
| `reference_audios` | URL array | Video Edit | Optional audio references, up to 10 |
| `last_image` | URL | Video Extend | Optional target frame for the continuation |
| `generate_audio` | boolean | Video Edit / Extend | Generate new synchronized audio; defaults to `true` |
| `aspect_ratio` | string | All routes | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, or `9:21` |
| `duration` | integer | All routes | `4`–`30` seconds; default `5` |
| `seed` | integer | All routes | `-1`–`4294967295`; use `-1` for random |
| `webhook_url` | URL | All routes | Optional completion webhook |

### Seedance Character (Consistent Character Sheets)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-character`

Create a multi-panel character sheet (front, back, side profile, action pose, facial expressions, accessories) at 4K / 21:9 from 1–3 reference photos of a real person.

Once the sheet is generated, pass its URL into `consistent_video()`, which anchors an Omni-Reference generation on it for consistent character identity across shots.

| Field | Type | Required | Description |
|---|---|---|---|
| `images_list` | array of URLs | Yes | 1–3 photos of the reference person |
| `prompt` | string | Yes | Desired outfit/style for the character |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2-character" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "images_list": ["https://example.com/person.jpg"],
      "prompt": "cyberpunk jacket with neon accents"
  }'
```

**Cost:** $0.18 per character sheet

For a full guide, see [CHARACTER_CONSISTENCY.md](CHARACTER_CONSISTENCY.md).

### Legacy Seedance 2.0 routes

The SDK also keeps `legacy_video_edit()` and `legacy_extend_video()` for
applications that still use the older request-ID based Seedance 2.0 routes.
Use `video_edit()` and `video_extend()` for the dedicated Seedance 2.5
Video Edit and Video Extend routes described above.

---

## 🎭 Character Consistency Workflow

Create a fictional character from reference photos and maintain their identity across multiple video scenes using the Omni-Reference endpoint.

See [CHARACTER_CONSISTENCY.md](CHARACTER_CONSISTENCY.md) for a full guide.

```python
from seedance_api import SeedanceAPI
api = SeedanceAPI()

# Step 1 — generate a character sheet (1–3 reference photos)
char = api.create_character(
    images_list=["https://example.com/person.jpg"],
    outfit_description="cyberpunk jacket with neon accents, glowing visor",
)
char_id = char["request_id"]
sheet_result = api.wait_for_completion(char_id)
sheet_url = sheet_result["outputs"][0]

# Step 2 — anchor a generation on the sheet via consistent_video() (Omni-Reference)
video = api.consistent_video(
    sheet_url=sheet_url,
    prompt="The character rides a motorcycle through a neon-lit city at night",
    aspect_ratio="16:9",
    duration=5,
)
result = api.wait_for_completion(video["request_id"])
print(f"Video: {result['outputs'][0]}")

# Add extra scene/prop reference images alongside the character sheet
video2 = api.consistent_video(
    sheet_url=sheet_url,
    prompt="The character draws their weapon in slow motion, dramatic lighting",
    aspect_ratio="16:9",
    duration=5,
    extra_images=["https://example.com/background.jpg"],
)
result2 = api.wait_for_completion(video2["request_id"])
print(f"Video: {result2['outputs'][0]}")
```

---

## 📖 Documentation & Guides

For prompt engineering and advanced use cases, see [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts).

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `generate` | `endpoint`, `prompt`, workflow-specific fields, `aspect_ratio`, `duration`, `seed` | Call any of the 72 Seedance 2.5 routes directly. |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Generate text-to-video; variant is `standard`, `intl`, or `spicy`, and resolution is `480p`, `720p`, `1080p`, or `4k`. |
| `text_to_video_480p` / `_1080p` / `_4k` | same as above | Convenience methods for standard or selected-variant resolution tiers. |
| `image_to_video` | `prompt`, `image_url`, `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Animate a single image. |
| `image_to_video_480p` / `_1080p` / `_4k` | same as above | Convenience methods for image-to-video resolution tiers. |
| `first_last_frame` | `prompt`, `images_list` (exactly 2), `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Keyframe transition between a start and end image. |
| `first_last_frame_480p` / `_1080p` / `_4k` | same as above | Convenience methods for keyframe resolution tiers. |
| `omni_reference` | `prompt`, `images_list`, `videos_list`, `audios_list`, `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Multimodal reference generation — up to 30 images / 10 videos / 10 audio clips. |
| `omni_reference_480p` / `_1080p` / `_4k` | same as above | Convenience methods for Omni Reference resolution tiers. |
| `video_edit` | `prompt`, `video`, `reference_images`, `reference_audios`, `generate_audio`, `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Edit an existing video through a dedicated Seedance 2.5 route. |
| `video_edit_480p` / `_1080p` / `_4k` | same as above | Convenience methods for Video Edit resolution tiers. |
| `video_extend` | `prompt`, `video`, `last_image`, `generate_audio`, `aspect_ratio`, `duration`, `seed`, `variant`, `resolution` | Continue an existing video from its last frame. |
| `video_extend_480p` / `_1080p` / `_4k` | same as above | Convenience methods for Video Extend resolution tiers. |
| `intl_*` / `spicy_*` | Same workflow fields plus `resolution` | Explicit helpers for the Intl and Spicy route families. |
| `create_character` | `images_list` (1–3), `outfit_description`, `character_name` | Generate a 4K character sheet from reference photos. Returns `request_id`; `outputs[0]` is the sheet URL. |
| `consistent_video` | `sheet_url`, `prompt`, `aspect_ratio`, `duration`, `extra_images` | Omni-Reference generation anchored on the character sheet. |
| `watermark_remover`| `video_url` | Remove MuAPI watermark from a Seedance video. |
| `watermark_remover_pro`| `video_url` | Remove MuAPI watermark from a Seedance video (Pro version). |
| `legacy_video_edit` | `prompt`, `video_urls`, `images_list`, `aspect_ratio`, `quality`, `remove_watermark`, `output_format` | Legacy Seedance 2.0 edit route. |
| `legacy_extend_video` | `request_id`, `prompt`, `duration`, `quality`, `output_format` | Legacy Seedance 2.0 extension route. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for the Seedance API. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for Seedance generation tasks. |

---

## 🔗 Official Resources
- **Playground — Seedance 2.5**:
  - [Text-to-Video](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Image-to-Video](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [First & Last Frame](https://muapi.ai/playground/seedance-2.5-first-last-frame?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Omni Reference](https://muapi.ai/playground/seedance-2.5-omni-reference?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
  - [Video Edit](https://muapi.ai/playground/seedance-2.5-video-edit?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Video Extend](https://muapi.ai/playground/seedance-2.5-video-extend?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
  - [Intl Text-to-Video](https://muapi.ai/playground/seedance-2.5-intl-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Spicy Text-to-Video](https://muapi.ai/playground/seedance-2.5-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.5 API, ByteDance Seedance, AI Video Generator, Text-to-Video AI, Image-to-Video API, Seedance Python SDK, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, AI Video Creation, ByteDance Video AI, Seedance API Documentation, Seedance I2V, Seedance T2V, AI Movie Generator, AI Animation API, Python Video API, Seedance 2.5 Tutorial.

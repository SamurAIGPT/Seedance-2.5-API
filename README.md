# Seedance 2.5 API: Python Wrapper for ByteDance's AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedance-2-5-api)

[![PyPI version](https://img.shields.io/pypi/v/seedance-2-api.svg)](https://pypi.org/project/seedance-2-api/)
[![GitHub stars](https://img.shields.io/github/stars/SamurAIGPT/Seedance-2.5-API.svg)](https://github.com/SamurAIGPT/Seedance-2.5-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2.5 API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api). Generate cinematic, high-fidelity AI videos from text prompts and static images — with industry-leading **realistic human face generation** — using ByteDance's most advanced video generation model.

Join the subreddit https://www.reddit.com/r/Seedance_2_API/ for discussions on using the Seedance 2.5 API.

> 🌟 **Seedance 2.5** ships as 8 early-access endpoints — Text-to-Video, Image-to-Video, First & Last Frame, and Omni-Reference, each with a 720p and a 480p tier. Clips up to 30s (up from 15s on 2.0). Omni-Reference accepts up to 20 reference images / 6 reference videos / 6 reference audio clips (up from 9/3/3 on Seedance 2.0). 480p/720p at launch — 1080p/4K are not yet available. Try it now: [I2V Playground](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [T2V Playground](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## 📺 Video Tutorial

[![How to Access Seedance 2.5 API (Step-by-Step Guide)](https://img.youtube.com/vi/Uszlw7H4VP4/maxresdefault.jpg)](https://www.youtube.com/watch?v=Uszlw7H4VP4)

**[How to Access Seedance 2.5 API (Step-by-Step Guide)](https://www.youtube.com/watch?v=Uszlw7H4VP4)** — a full walkthrough of getting an API key and making your first Seedance 2.5 call via [MuAPI](https://muapi.ai/seedance-2.5?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api).

## Related Projects

- [seedance-2.0-watermark-remover](https://github.com/SamurAIGPT/seedance-2.0-watermark-remover) — Remove watermarks from your Seedance generated videos
- [seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) — Ready-made Next.js SaaS built on Seedance 2
- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper covering Seedance 2.0 and Seedance 2 Mini
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide, prompts, camera controls, and video generation examples
- [seedance2.5-comfyui](https://github.com/Anil-matcha/seedance2.5-comfyui) — Native Seedance 2.5 ComfyUI custom nodes and example workflows
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper for Black Forest Labs' FLUX 3 Text-to-Video and Image-to-Video

## 🚀 Why Use Seedance 2.5 API?

Seedance 2.5 is ByteDance's most advanced video generation model, offering unparalleled video quality and motion consistency.

- **Longer Clips**: Generate up to 30 seconds per clip (up from 15s on Seedance 2.0).
- **Realistic Human Faces**: Best-in-class facial fidelity — natural expressions, skin detail, and identity consistency across frames.
- **Less Censorship**: More permissive content policy compared to other AI video models, enabling a wider range of creative use cases.
- **Superior Motion Control**: Advanced camera movement and improved character consistency for professional results.
- **Multimodal API**: Supports Text-to-Video (T2V), Image-to-Video (I2V), First & Last Frame keyframe transitions, and Omni-Reference.
- **Developer-First**: Fast processing via the MuAPI infrastructure with a simple Python SDK.

## 🌟 Key Features of Seedance 2.5 API

- ✅ **Realistic Human Face Generation**: Produces natural, high-fidelity human faces with accurate expressions, skin texture, and identity consistency — no uncanny valley.
- ✅ **Seedance 2.5 Text-to-Video (T2V)**: Transform complex descriptive prompts into stunning AI video clips, up to 30s long.
- ✅ **Seedance 2.5 Image-to-Video (I2V)**: Animate a single static image with precise motion control using `image_url`.
- ✅ **Seedance 2.5 First & Last Frame**: Generate a smooth keyframe-driven transition between a start and end image.
- ✅ **Seedance 2.5 Omni-Reference**: Condition a video on any combination of image, video, and audio references in one request — up to 20 reference images, 6 reference videos, and 6 reference audio clips (up from 9/3/3 on Seedance 2.0).
- ✅ **Seedance Character**: Generate a multi-panel character sheet (front, back, side, action pose, expressions) from 1–3 reference photos, then anchor an Omni-Reference generation on it via `consistent_video()` for consistent identity across shots.
- ✅ **480p Tiers**: Every Seedance 2.5 endpoint has a faster, cheaper 480p variant alongside the 720p default.
- ✅ **Reproducible Seeds**: Pass `seed` to keep generations in the same neighborhood across repeated calls.
- ✅ **File Upload**: Directly upload local images and videos using the `upload_file` method, supporting seamless use in generation tasks.
- ✅ **Less Censorship**: More permissive content policy than competing models — broader creative freedom out of the box.
- ✅ **Flexible Aspect Ratios**: `16:9`, `9:16` (TikTok/Reels), `1:1`, `4:3`, `3:4`, `21:9`, `9:21`.

> **Resolution note**: Seedance 2.5 supports `480p` and `720p` at launch. `1080p` and `4K` are not yet available on this model.
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
print(f"Success! View your Seedance 2.5 video here: {result['url']}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedance 2.5 Text-to-Video (T2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-text-to-video` ($0.60/sec, 720p)
**480p tier**: `POST https://api.muapi.ai/api/v1/seedance-2.5-text-to-video-480p` ($0.30/sec)
**Playground**: [720p](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-text-to-video-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas",
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 2. Seedance 2.5 Image-to-Video (I2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-image-to-video` ($0.60/sec, 720p)
**480p tier**: `POST https://api.muapi.ai/api/v1/seedance-2.5-image-to-video-480p` ($0.30/sec)
**Playground**: [720p](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-image-to-video-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

Takes a single `image_url` (not a list) plus a `prompt`.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Make the clouds move slowly across the sky",
      "image_url": "https://example.com/mountain.jpg",
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 2b. Seedance 2.5 Spicy (T2V / I2V)
**Endpoints**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-text-to-video` · `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-image-to-video` ($0.60/sec, 720p only — no 480p tier)
**Playground**: [T2V](https://muapi.ai/playground/seedance-2.5-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [I2V](https://muapi.ai/playground/seedance-2.5-spicy-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

Relaxed-moderation siblings of the flagship T2V/I2V models — same request shape, same pricing, more permissive content policy.

### 3. Seedance 2.5 First & Last Frame
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-first-last-frame` ($0.60/sec, 720p)
**480p tier**: `POST https://api.muapi.ai/api/v1/seedance-2.5-first-last-frame-480p` ($0.30/sec)
**Playground**: [720p](https://muapi.ai/playground/seedance-2.5-first-last-frame?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-first-last-frame-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

Generates a smooth keyframe-driven transition between a start and end image. `images_list` must be exactly `[first_frame_url, last_frame_url]`.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-first-last-frame" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Smooth cinematic transition as the scene shifts from day to night",
      "images_list": ["https://example.com/start.jpg", "https://example.com/end.jpg"],
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 4. Seedance 2.5 Omni-Reference
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-omni-reference` ($0.72/sec, 720p)
**480p tier**: `POST https://api.muapi.ai/api/v1/seedance-2.5-omni-reference-480p` ($0.36/sec)
**Playground**: [720p](https://muapi.ai/playground/seedance-2.5-omni-reference?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-omni-reference-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

Condition a single video generation on any combination of image, video, and audio references — up to 20 images, 6 videos, and 6 audio clips.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-omni-reference" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A dramatic chase scene through a neon city, matching the style of the reference image and rhythm of the reference video",
      "aspect_ratio": "16:9",
      "duration": 5,
      "images_list": ["https://example.com/scene_ref.jpg"],
      "videos_list": ["https://example.com/style_ref.mp4"]
  }'
```

### 5. Seedance Character (Consistent Character Sheets)
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

### 6. Seedance 2.0 Video-Edit & Extend

There is no dedicated Seedance 2.5 video-edit or extend endpoint yet. `video_edit()` and `extend_video()` fall back to the Seedance 2.0 endpoints below, which work on any Seedance-family request_id/video.

**Video-Edit endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-video-edit`
```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-video-edit" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The cat walks through a garden",
      "video_urls": ["https://example.com/video.mp4"],
      "images_list": ["https://example.com/image.jpg"],
      "aspect_ratio": "16:9",
      "quality": "basic",
      "remove_watermark": false
  }'
```

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
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `seed` | Generate 720p video from text, up to 30s. |
| `text_to_video_480p` | `prompt`, `aspect_ratio`, `duration`, `seed` | 480p tier — faster/cheaper. |
| `image_to_video` | `prompt`, `image_url`, `aspect_ratio`, `duration`, `seed` | Animate a single image at 720p. |
| `image_to_video_480p` | `prompt`, `image_url`, `aspect_ratio`, `duration`, `seed` | 480p tier — faster/cheaper. |
| `spicy_text_to_video` | `prompt`, `aspect_ratio`, `duration`, `seed` | Relaxed-moderation T2V at 720p. No 480p tier. |
| `spicy_image_to_video` | `prompt`, `image_url`, `aspect_ratio`, `duration`, `seed` | Relaxed-moderation I2V at 720p. No 480p tier. |
| `first_last_frame` | `prompt`, `images_list` (exactly 2), `aspect_ratio`, `duration`, `seed` | Keyframe transition between a start and end image at 720p. |
| `first_last_frame_480p` | `prompt`, `images_list` (exactly 2), `aspect_ratio`, `duration`, `seed` | 480p tier — faster/cheaper. |
| `omni_reference` | `prompt`, `aspect_ratio`, `duration`, `images_list`, `videos_list`, `audios_list`, `seed` | Multi-modal reference video generation at 720p — up to 20 images / 6 videos / 6 audio clips. |
| `omni_reference_480p` | same as above | 480p tier — faster/cheaper. |
| `create_character` | `images_list` (1–3), `outfit_description`, `character_name` | Generate a 4K character sheet from reference photos. Returns `request_id`; `outputs[0]` is the sheet URL. |
| `consistent_video` | `sheet_url`, `prompt`, `aspect_ratio`, `duration`, `extra_images` | Omni-Reference generation anchored on the character sheet. |
| `video_edit` | `prompt`, `video_urls`, `images_list`, `aspect_ratio`, `quality`, `remove_watermark`, `output_format` | Edit existing videos with prompts and images (Seedance 2.0 endpoint). |
| `watermark_remover`| `video_url` | Remove MuAPI watermark from a Seedance video. |
| `watermark_remover_pro`| `video_url` | Remove MuAPI watermark from a Seedance video (Pro version). |
| `extend_video` | `request_id`, `prompt`, `duration`, `quality`, `output_format` | Extend an existing Seedance video segment (Seedance 2.0 endpoint). |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for the Seedance API. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for Seedance generation tasks. |

---

## 🔗 Official Resources
- **Playground — Seedance 2.5**:
  - Text-to-Video: [720p](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-text-to-video-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Spicy](https://muapi.ai/playground/seedance-2.5-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
  - Image-to-Video: [720p](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-image-to-video-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [Spicy](https://muapi.ai/playground/seedance-2.5-spicy-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
  - First & Last Frame: [720p](https://muapi.ai/playground/seedance-2.5-first-last-frame?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-first-last-frame-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
  - Omni-Reference: [720p](https://muapi.ai/playground/seedance-2.5-omni-reference?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [480p](https://muapi.ai/playground/seedance-2.5-omni-reference-480p?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.5 API, ByteDance Seedance, AI Video Generator, Text-to-Video AI, Image-to-Video API, Seedance Python SDK, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, AI Video Creation, ByteDance Video AI, Seedance API Documentation, Seedance I2V, Seedance T2V, AI Movie Generator, AI Animation API, Python Video API, Seedance 2.5 Tutorial.

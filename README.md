# Seedance 2.5 API: Python Wrapper for ByteDance's AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedance-2-5-api)

[![PyPI version](https://img.shields.io/pypi/v/seedance-2-api.svg)](https://pypi.org/project/seedance-2-api/)
[![GitHub stars](https://img.shields.io/github/stars/SamurAIGPT/Seedance-2.5-API.svg)](https://github.com/SamurAIGPT/Seedance-2.5-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2.5 API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api). Generate cinematic, high-fidelity AI videos from text prompts and static images — with industry-leading **realistic human face generation** — using ByteDance's most advanced video generation model.

Join the subreddit https://www.reddit.com/r/Seedance_2_API/ for discussions on using the Seedance 2.5 API.

> 🌟 **Seedance 2.5** — clips up to 30s (up from 15s), 30 reference images / 10 reference videos / 10 reference audio clips per request (up from 9/3/3), synced audio generation, fixed-camera control, and improved character consistency over Seedance 2.0. 480p/720p at launch — 1080p/4K are not yet available. Try it now: [I2V Playground](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [T2V Playground](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## Related Projects

- [seedance-2.0-watermark-remover](https://github.com/SamurAIGPT/seedance-2.0-watermark-remover) — Remove watermarks from your Seedance generated videos
- [seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) — Ready-made Next.js SaaS built on Seedance 2
- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper covering Seedance 2.0 and Seedance 2 Mini
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide, prompts, camera controls, and video generation examples

## 🚀 Why Use Seedance 2.5 API?

Seedance 2.5 is ByteDance's most advanced video generation model, offering unparalleled video quality and motion consistency.

- **Longer Clips**: Generate up to 30 seconds per clip (up from 15s on Seedance 2.0).
- **Realistic Human Faces**: Best-in-class facial fidelity — natural expressions, skin detail, and identity consistency across frames.
- **Less Censorship**: More permissive content policy compared to other AI video models, enabling a wider range of creative use cases.
- **Superior Motion Control**: Advanced camera movement (including a fixed-camera option) and character consistency for professional results.
- **Multimodal API**: Supports Text-to-Video (T2V), Image-to-Video (I2V), and Video Extension.
- **Developer-First**: Fast processing via the MuAPI infrastructure with a simple Python SDK.

## 🌟 Key Features of Seedance 2.5 API

- ✅ **Realistic Human Face Generation**: Produces natural, high-fidelity human faces with accurate expressions, skin texture, and identity consistency — no uncanny valley.
- ✅ **Seedance 2.5 Text-to-Video (T2V)**: Transform complex descriptive prompts into stunning AI video clips, up to 30s long.
- ✅ **Seedance 2.5 Image-to-Video (I2V)**: Animate any static image with precise motion control using `images_list`.
- ✅ **Seedance 2.5 Omni-Reference**: Condition a video on any combination of image, video, and audio references in one request — up to 30 reference images, 10 reference videos, and 10 reference audio clips (up from 9/3/3 on Seedance 2.0).
- ✅ **Seedance 2.5 Character**: Generate a multi-panel character sheet (front, back, side, action pose, expressions) from 1–3 reference photos. Use `@character:<id>` inline in any prompt, or pass the sheet directly as an anchor image for tighter face fidelity via `consistent_video()`.
- ✅ **Seedance 2.5 Video-Edit**: Edit existing videos using text prompts and reference images for stylized results.
- ✅ **Synced Audio Generation**: `generate_audio` produces voice, sound effects, and background music matched to the visuals — wrap dialogue in quotes for best results.
- ✅ **Fixed-Camera Control**: `camera_fixed` biases the model toward a static, non-moving shot.
- ✅ **High-Fidelity Output Format**: `output_format="mov"` (yuv444p + PCM audio) avoids the color drift and audio desync that accumulate across repeated extensions/edits with `mp4` — recommended whenever a clip will be extended or re-edited multiple times. Seedance 2.5 only.
- ✅ **File Upload**: Directly upload local images and videos using the `upload_file` method, supporting seamless use in generation tasks.
- ✅ **Less Censorship**: More permissive content policy than competing models — broader creative freedom out of the box.
- ✅ **Flexible Aspect Ratios**: Optimized for `16:9`, `9:16` (TikTok/Reels), `4:3`, `3:4`, `1:1`, and `21:9`.

> **Resolution note**: Seedance 2.5 supports `480p` and `720p` at launch. `1080p` and `4K` are not yet available on this model.

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
    quality="high"
)

# 2. Wait for completion
result = api.wait_for_completion(submission['request_id'])
print(f"Success! View your Seedance 2.5 video here: {result['url']}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedance 2.5 Text-to-Video (T2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-t2v`

Supports `@character:<id>` inline in the prompt — see [Character Workflow](#-character-consistency-workflow) below.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-t2v" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas",
      "aspect_ratio": "16:9",
      "duration": 5,
      "quality": "high"
  }'
```

### 2. Seedance 2.5 Image-to-Video (I2V)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-i2v`

Reference images with `@image1`, `@image2`, etc. in the prompt. Supports `@character:<id>` — characters are automatically appended to `images_list`.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-v2.0-i2v" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Make the clouds move slowly across the sky",
      "images_list": ["https://example.com/mountain.jpg"],
      "aspect_ratio": "16:9",
      "duration": 5,
      "quality": "basic"
  }'
```

### 3. Seedance 2.5 Omni-Reference
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.0-omni-reference`

Condition a single video generation on any combination of image, video, and audio references. Use `@character:<id>` inline in the prompt to inject a character (see section below).

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.0-omni-reference" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A dramatic chase scene through a neon city",
      "aspect_ratio": "16:9",
      "duration": 5,
      "images_list": ["https://example.com/scene_ref.jpg"],
      "video_files": ["https://example.com/style_ref.mp4"]
  }'
```

### 4. Seedance 2.5 Character (Consistent Character Sheets)
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-character`

Create a multi-panel character sheet (front, back, side profile, action pose, facial expressions, accessories) at 4K / 21:9 from 1–3 reference photos of a real person.

Once the sheet is generated you can use it two ways:
- **`@character:<request_id>`** inline in any T2V, I2V, or Omni-Reference prompt
- Pass `outputs[0]` (the sheet image URL) directly as `@image1` in an I2V request for tighter face fidelity via `consistent_video()`

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

For a full guide including the direct sheet-anchored I2V workflow, see [CHARACTER_CONSISTENCY.md](CHARACTER_CONSISTENCY.md).

### 5. Seedance 2.5 Video-Edit
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-v2.0-video-edit`
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

Create a fictional character from reference photos and maintain their identity across multiple video scenes.

See [CHARACTER_CONSISTENCY.md](CHARACTER_CONSISTENCY.md) for a full guide.

### Option A — `@character:<id>` inline (simplest)

```python
from seedance_api import SeedanceAPI
api = SeedanceAPI()

# Step 1 — generate a character sheet (1–3 reference photos)
char = api.create_character(
    images_list=["https://example.com/person.jpg"],
    outfit_description="cyberpunk jacket with neon accents, glowing visor",
)
char_id = char["request_id"]
api.wait_for_completion(char_id)  # wait for sheet to render

# Step 2 — reference the character inline in any prompt
video = api.text_to_video(
    prompt=f"@character:{char_id} rides a motorcycle through a neon-lit city at night",
    aspect_ratio="16:9",
    duration=5,
)
result = api.wait_for_completion(video["request_id"])
print(f"Video: {result['outputs'][0]}")

# Multiple characters in one prompt
char2_id = "another-completed-character-request-id"
video2 = api.text_to_video(
    prompt=f"@character:{char_id} and @character:{char2_id} face off in a neon-lit arena",
    aspect_ratio="16:9",
    duration=5,
)
```

### Option B — `consistent_video()` (tighter face fidelity)

Pass the character sheet directly as the anchor image for Image-to-Video generation.

```python
# Get the sheet URL after character creation
sheet_result = api.wait_for_completion(char_id)
sheet_url = sheet_result["outputs"][0]

# Generate with the sheet as anchor
video = api.consistent_video(
    sheet_url=sheet_url,
    prompt="@image1 draws their weapon in slow motion, dramatic lighting",
    aspect_ratio="16:9",
    duration=5,
    quality="high",
)
result = api.wait_for_completion(video["request_id"])
print(f"Video: {result['outputs'][0]}")
```

> **Tip**: `@character:<id>` works in T2V, I2V, and Omni-Reference prompts. Use `consistent_video()` when face similarity is critical.

---

## 📖 Documentation & Guides

For prompt engineering and advanced use cases, see [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts).

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `quality`, `remove_watermark`, `generate_audio`, `camera_fixed`, `output_format` | Generate video from text, up to 30s. Supports `@character:<id>` in prompt. |
| `image_to_video` | `prompt`, `images_list`, `aspect_ratio`, `duration`, `quality`, `remove_watermark`, `generate_audio`, `camera_fixed`, `output_format` | Animate images. Supports `@image1`/`@character:<id>` in prompt. |
| `omni_reference` | `prompt`, `aspect_ratio`, `duration`, `quality`, `images_list`, `video_files`, `audio_files`, `generate_audio`, `camera_fixed`, `output_format` | Multi-modal reference video generation — up to 30 images / 10 videos / 10 audio clips. |
| `create_character` | `images_list` (1–3), `outfit_description`, `character_name` | Generate a 4K character sheet from reference photos. Returns `request_id`; `outputs[0]` is the sheet URL. |
| `consistent_video` | `sheet_url`, `prompt`, `aspect_ratio`, `duration`, `quality`, `extra_images` | I2V with the character sheet as anchor (`@image1`). Tighter face fidelity than `@character:<id>`. |
| `video_edit` | `prompt`, `video_urls`, `images_list`, `aspect_ratio`, `quality`, `remove_watermark`, `output_format` | Edit existing videos with prompts and images. |
| `watermark_remover`| `video_url` | Remove MuAPI watermark from a Seedance video. |
| `watermark_remover_pro`| `video_url` | Remove MuAPI watermark from a Seedance video (Pro version). |
| `text_to_video_480p`| `prompt`, `aspect_ratio`, `duration`, `quality` | Generate a 480p video from text (faster/cheaper). |
| `image_to_video_480p`| `prompt`, `images_list`, `aspect_ratio`, `duration`, `quality` | Generate a 480p video from an image (faster/cheaper). |
| `extend_video` | `request_id`, `prompt`, `duration`, `quality`, `output_format` | Extend an existing Seedance video segment, up to a combined 30s. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for the Seedance API. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for Seedance generation tasks. |

---

## 🔗 Official Resources
- **Playground — Seedance 2.5**: [I2V](https://muapi.ai/playground/seedance-2.5-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api) · [T2V](https://muapi.ai/playground/seedance-2.5-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-5-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.5 API, ByteDance Seedance, AI Video Generator, Text-to-Video AI, Image-to-Video API, Seedance Python SDK, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, AI Video Creation, ByteDance Video AI, Seedance API Documentation, Seedance I2V, Seedance T2V, AI Movie Generator, AI Animation API, Python Video API, Seedance 2.5 Tutorial.

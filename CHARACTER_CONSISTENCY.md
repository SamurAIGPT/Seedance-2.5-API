# Seedance 2.5 — Character Consistency

Generate videos featuring the same fictional character across multiple scenes using the Seedance 2.5 character workflow.

---

## How It Works

The workflow has two steps:

1. **Create a character sheet** — Upload 1–3 reference photos of a real person plus an outfit/style description. The API renders a structured character sheet (front view, back view, side profile, action pose, facial expressions, accessories) at 4K / 21:9. You receive a `request_id` and, once completed, a `sheet_url`.
2. **Use the character in videos** — Two options:
   - **`@character:<request_id>`** — reference the character inline in any T2V, I2V, or Omni-Reference prompt. The server resolves the sheet automatically.
   - **`consistent_video()` / direct I2V** — pass the `sheet_url` as the first image in an Image-to-Video request (recommended for tighter face/identity preservation).

---

## Step 1 — Create a Character

**Endpoint:** `POST /api/v1/seedance-2-character`

| Field | Type | Required | Description |
|---|---|---|---|
| `images_list` | array of URLs | Yes | 1–3 photos of the reference person |
| `prompt` | string | Yes | Desired outfit/style for the character |

**Example request:**
```json
{
  "images_list": ["https://example.com/person.jpg"],
  "prompt": "cyberpunk jacket with neon blue accents, black tactical pants, worn boots"
}
```

**Example response:**
```json
{
  "request_id": "ab539e5f-1234-5678-abcd-ef0123456789"
}
```

Poll `GET /api/v1/predictions/<request_id>/result` until `status` is `completed`. The result `outputs[0]` contains the character sheet image URL.

**Cost:** $0.18 per character sheet

---

## Step 2 — Use the Character in a Video

### Option A — `@character:<id>` inline (easiest)

Once the character sheet is ready, embed it in any prompt with:

```
@character:<request_id>
```

#### Text-to-Video

```json
{
  "prompt": "@character:ab539e5f-1234-... walks through a rain-soaked neon city at night",
  "aspect_ratio": "16:9",
  "duration": 5,
  "quality": "basic"
}
```

#### Image-to-Video

```json
{
  "prompt": "@character:ab539e5f-1234-... looks out over the city from a rooftop",
  "images_list": ["https://example.com/background.jpg"],
  "aspect_ratio": "16:9",
  "duration": 5
}
```

#### Omni-Reference (image + video + audio)

```json
{
  "prompt": "@character:ab539e5f-1234-... enters the scene and picks up the artifact",
  "aspect_ratio": "16:9",
  "duration": 6,
  "images_list": ["https://example.com/scene.jpg"],
  "video_files": ["https://example.com/intro_clip.mp4"]
}
```

#### Multiple Characters

You can reference more than one character in the same prompt:

```
"@character:ab539e5f-... and @character:cd781a2b-... face each other in the arena"
```

---

### Option B — Direct Image-to-Video with sheet_url (tighter face fidelity)

Pass the character sheet image directly as `@image1` in an I2V request. This gives the model the full 4K sheet at inference time rather than resolving it server-side, which can improve face similarity.

```json
{
  "prompt": "@image1 rides a motorcycle through a neon-lit city at night, cinematic",
  "images_list": ["<sheet_url from completed character request>"],
  "aspect_ratio": "16:9",
  "duration": 5,
  "quality": "high"
}
```

---

## Python Example

```python
from seedance_api import SeedanceAPI

api = SeedanceAPI()

# Step 1 — Create the character
char = api.create_character(
    images_list=["https://example.com/person.jpg"],
    outfit_description="cyberpunk jacket with neon blue accents, black tactical pants",
)
char_id = char["request_id"]
print(f"Character ID: {char_id}")

# Wait for the character sheet to render
sheet_result = api.wait_for_completion(char_id)
sheet_url = sheet_result["outputs"][0]
print(f"Character sheet: {sheet_url}")

# Step 2a — Use @character:<id> in T2V (simplest)
video = api.text_to_video(
    prompt=f"@character:{char_id} rides a motorcycle through a neon-lit city at night",
    aspect_ratio="16:9",
    duration=5,
    quality="basic"
)
result = api.wait_for_completion(video["request_id"])
print(f"Video URL: {result['outputs'][0]}")

# Step 2b — Use consistent_video() for tighter face preservation
video2 = api.consistent_video(
    sheet_url=sheet_url,
    prompt="@image1 draws their weapon in slow motion, dramatic lighting",
    aspect_ratio="16:9",
    duration=5,
    quality="high",
)
result2 = api.wait_for_completion(video2["request_id"])
print(f"Video URL: {result2['outputs'][0]}")
```

---

## Tips for Best Results

- **Reference photos:** Use 2–3 clear, well-lit shots — a frontal, a 3/4-angle, and a side profile. Avoid heavy shadows or obscured faces.
- **Outfit description:** Be specific — mention materials, colors, and distinctive details. Vague descriptions produce generic outfits.
- **Prompt framing:** Describe what the character *does*, not what they *look like* — the sheet already carries the visual identity.
- **Consistency across scenes:** Reuse the same `char_id` or `sheet_url` across all shots in a series to keep the character identical.
- **Duration:** For scenes with complex character movement, use `duration=8` and `quality=high` for smoother results.
- **Face fidelity:** If `@character:<id>` produces drifting features, switch to `consistent_video()` (Option B) which anchors directly on the sheet image.

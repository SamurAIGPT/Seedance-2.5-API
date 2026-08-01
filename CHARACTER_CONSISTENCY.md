# Seedance — Character Consistency

Generate videos featuring the same fictional character across multiple scenes.

---

## How It Works

The workflow has two steps:

1. **Create a character sheet** — Upload 1–3 reference photos of a real person plus an outfit/style description. The API renders a structured character sheet (front view, back view, side profile, action pose, facial expressions, accessories) at 4K / 21:9. You receive a `request_id` and, once completed, a `sheet_url`.
2. **Anchor a video on the sheet** — Pass `sheet_url` into `consistent_video()`, which submits it as a reference image on the Seedance 2.5 **Omni-Reference** endpoint (the only current Seedance 2.5 endpoint that accepts more than one input image). Describe what the character does in the prompt — the sheet already carries the visual identity.

> There is no `@character:<id>` API field — the model resolves identity purely from the reference image(s) you pass, described in your prompt.

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

## Step 2 — Anchor a Video on the Character (Omni-Reference)

**Endpoint:** `POST /api/v1/seedance-2.5-omni-reference` (or the `-480p` tier)

Pass the character sheet as one of `images_list`. You can add extra reference images (background, props, style refs) alongside it — up to 20 total.

```json
{
  "prompt": "The character from the reference image rides a motorcycle through a neon-lit city at night, cinematic",
  "images_list": ["<sheet_url from completed character request>"],
  "aspect_ratio": "16:9",
  "duration": 5
}
```

To keep a character consistent across a series of shots, reuse the same `sheet_url` as the first entry in `images_list` on every generation, and describe the character's distinguishing features (outfit, hair, build) in the prompt each time — the model doesn't retain state between requests.

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

# Step 2 — Anchor a video generation on the sheet via consistent_video()
video = api.consistent_video(
    sheet_url=sheet_url,
    prompt="The character rides a motorcycle through a neon-lit city at night, cinematic",
    aspect_ratio="16:9",
    duration=5,
)
result = api.wait_for_completion(video["request_id"])
print(f"Video URL: {result['outputs'][0]}")

# Add more scene/prop reference images alongside the character sheet
video2 = api.consistent_video(
    sheet_url=sheet_url,
    prompt="The character draws their weapon in slow motion, dramatic lighting, matching the rooftop background",
    aspect_ratio="16:9",
    duration=5,
    extra_images=["https://example.com/rooftop-background.jpg"],
)
result2 = api.wait_for_completion(video2["request_id"])
print(f"Video URL: {result2['outputs'][0]}")
```

---

## Tips for Best Results

- **Reference photos:** Use 2–3 clear, well-lit shots — a frontal, a 3/4-angle, and a side profile. Avoid heavy shadows or obscured faces.
- **Outfit description:** Be specific — mention materials, colors, and distinctive details. Vague descriptions produce generic outfits.
- **Prompt framing:** Describe what the character *does*, not what they *look like* — the sheet already carries the visual identity.
- **Consistency across scenes:** Reuse the same `sheet_url` as the first `images_list` entry across all shots in a series to keep the character identical.
- **Duration:** For scenes with complex character movement, use `duration=8`–`10` for smoother results.

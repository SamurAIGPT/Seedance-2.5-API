---
name: seedance-v2
description: Generate cinematic, high-fidelity AI videos with the Seedance 2.5 API (by ByteDance) through MuAPI.
version: 1.1.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🎥
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Seedance 2.5

Seedance 2.5 is ByteDance's high-fidelity video generation model. This skill
supports text-to-video, image animation, keyframe transitions, multimodal
references, video editing, video extension, and character workflows.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

You can select standard, Intl, or Spicy route variants and 480p, 720p,
upscaled 1080p, or upscaled 4K tiers. Durations range from 4 to 30 seconds.

### Text-to-Video (T2V)
Generate a video from a descriptive text prompt.
```bash
python3.11 skills/seedance-v2/seedance_cli.py t2v --prompt "A cinematic slow-motion shot of a cyberpunk city in the rain" --variant intl --resolution 1080p --wait
```

### Image-to-Video (I2V)
Animate one static image.
```bash
python3.11 skills/seedance-v2/seedance_cli.py i2v --image_url "https://example.com/image.jpg" --prompt "Make the clouds move slowly" --wait
```

### First & Last Frame
Generate a transition between exactly two images.
```bash
python3.11 skills/seedance-v2/seedance_cli.py first-last --images "https://example.com/start.jpg" "https://example.com/end.jpg" --prompt "Smoothly transition from day to night" --wait
```

### Video Rendering & Editing
Edit an existing video or apply styles.
```bash
python3.11 skills/seedance-v2/seedance_cli.py edit --video "https://example.com/video.mp4" --prompt "Turn the sunny afternoon into a rainy blue-hour scene" --wait
```

### Omni-Reference Generation
Condition videos on any combination of images, videos, and audio.
```bash
python3.11 skills/seedance-v2/seedance_cli.py omni --prompt "The character @character:ID dances in the rain" --images "https://example.com/bg.jpg" --videos "https://example.com/motion.mp4" --wait
```

### Character Consistency
Create a reusable character sheet for consistent generation.
```bash
python3.11 skills/seedance-v2/seedance_cli.py character --images "https://example.com/face.jpg" --outfit "Cyberpunk neon jacket" --name "Neo" --wait
```

### Watermark Removal
Remove MuAPI watermarks from generated videos.
```bash
python3.11 skills/seedance-v2/seedance_cli.py watermark-remover --video_url "https://api.muapi.ai/..." --wait
```

### Extending Videos
Continue an existing video from its final frame.
```bash
python3.11 skills/seedance-v2/seedance_cli.py extend --video "https://example.com/video.mp4" --prompt "Continue the camera move into the city" --wait
```

### Any route
Use the `generate` command when you need an exact route slug, including any
Intl or Spicy resolution variant.
```bash
python3.11 skills/seedance-v2/seedance_cli.py generate --endpoint seedance-2.5-spicy-video-edit-4k --video "https://example.com/video.mp4" --prompt "Change the lighting to a neon night scene" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed prompts result in better video quality and more accurate motion.
- **Wait for Completion**: Use the `--wait` flag to receive the final video URL directly. Without it, you will receive a `request_id` which you can check later using the `status` command.
- **Aspect Ratios**: Use `16:9` for horizontal videos and `9:16` for vertical content (like TikTok or Reels).
- **Resolution**: Select the route tier with `--resolution`; 1080p and 4K are upscaled from the 720p base render.
- **Variants**: Use `--variant intl` for the international route or `--variant spicy` for the relaxed-content-safety route.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2v` | `--prompt`, `--variant`, `--resolution`, `--aspect_ratio`, `--duration`, `--seed`, `--wait` | Text to Video |
| `i2v` | `--image_url`, `--prompt`, `--variant`, `--resolution`, `--aspect_ratio`, `--duration`, `--seed`, `--wait` | Image to Video |
| `first-last` | `--images` (exactly 2), `--prompt`, `--variant`, `--resolution`, `--aspect_ratio`, `--duration`, `--seed`, `--wait` | First & Last Frame |
| `omni` | `--prompt`, `--images`, `--videos`, `--audios`, `--variant`, `--resolution`, `--aspect_ratio`, `--duration`, `--seed`, `--wait` | Omni Reference |
| `character` | `--images`, `--outfit`, `--name`, `--wait` | Create Character Sheet |
| `edit` | `--prompt`, `--video`, `--variant`, `--resolution`, `--reference-images`, `--reference-audios`, `--no-audio`, `--wait` | Video Edit |
| `watermark-remover` | `--video_url`, `--wait` | Remove Watermark |
| `extend` | `--prompt`, `--video`, `--last-image`, `--variant`, `--resolution`, `--no-audio`, `--wait` | Video Extend |
| `generate` | `--endpoint`, `--prompt`, workflow-specific input flags, `--wait` | Any current Seedance 2.5 route |
| `status`| `--request_id` | Check Task Status |

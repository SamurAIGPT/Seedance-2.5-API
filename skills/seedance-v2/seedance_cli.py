import argparse
import json
import os
import sys


# Add the repository root so the skill can import seedance_api.py.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from seedance_api import SEEDANCE_25_ENDPOINTS, SeedanceAPI


RESOLUTIONS = ["480p", "720p", "1080p", "4k"]


def add_video_options(parser):
    parser.add_argument("--aspect_ratio", default="16:9", help="Output aspect ratio")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds")
    parser.add_argument("--seed", type=int, help="Optional reproducibility seed")
    parser.add_argument("--wait", action="store_true", help="Wait for completion")


def print_result(api, result, wait):
    request_id = result.get("request_id")
    if wait and request_id:
        print("Task submitted: {}. Waiting for completion...".format(request_id))
        result = api.wait_for_completion(request_id)
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Seedance 2.5 CLI for MuAPI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    t2v = subparsers.add_parser("t2v", help="Generate video from text")
    t2v.add_argument("--prompt", required=True, help="Text prompt")
    t2v.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    t2v.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    add_video_options(t2v)

    i2v = subparsers.add_parser("i2v", help="Generate video from one image")
    i2v.add_argument("--prompt", required=True, help="Motion prompt")
    i2v.add_argument("--image_url", required=True, help="Input image URL")
    i2v.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    i2v.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    add_video_options(i2v)

    first_last = subparsers.add_parser("first-last", help="Generate between two keyframe images")
    first_last.add_argument("--prompt", required=True, help="Transition prompt")
    first_last.add_argument("--images", required=True, nargs=2, help="First-frame and last-frame URLs")
    first_last.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    first_last.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    add_video_options(first_last)

    omni = subparsers.add_parser("omni", help="Generate with image, video, and audio references")
    omni.add_argument("--prompt", required=True, help="Text prompt")
    omni.add_argument("--images", nargs="*", help="Reference image URLs")
    omni.add_argument("--videos", nargs="*", help="Reference video URLs")
    omni.add_argument("--audios", nargs="*", help="Reference audio URLs")
    omni.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    omni.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    add_video_options(omni)

    edit = subparsers.add_parser("edit", help="Edit an existing video")
    edit.add_argument("--prompt", required=True, help="Edit prompt")
    edit.add_argument("--video", required=True, help="Video URL to edit")
    edit.add_argument("--reference-images", nargs="*", help="Optional reference image URLs")
    edit.add_argument("--reference-audios", nargs="*", help="Optional reference audio URLs")
    edit.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    edit.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    edit.add_argument("--no-audio", action="store_true", help="Do not generate new audio")
    add_video_options(edit)

    extend = subparsers.add_parser("extend", help="Continue an existing video")
    extend.add_argument("--prompt", required=True, help="Continuation prompt")
    extend.add_argument("--video", required=True, help="Video URL to extend")
    extend.add_argument("--last-image", help="Optional target frame URL")
    extend.add_argument("--variant", choices=["standard", "intl", "spicy"], default="standard")
    extend.add_argument("--resolution", choices=RESOLUTIONS, default="720p")
    extend.add_argument("--no-audio", action="store_true", help="Do not generate new audio")
    add_video_options(extend)

    generate = subparsers.add_parser("generate", help="Call any current Seedance 2.5 route")
    generate.add_argument("--endpoint", required=True, choices=sorted(SEEDANCE_25_ENDPOINTS))
    generate.add_argument("--prompt", required=True, help="Text prompt")
    generate.add_argument("--image-url", dest="image_url", help="Single I2V image URL")
    generate.add_argument("--images", nargs="*", help="First/last or Omni Reference image URLs")
    generate.add_argument("--videos", nargs="*", help="Omni Reference video URLs")
    generate.add_argument("--audios", nargs="*", help="Omni Reference audio URLs")
    generate.add_argument("--video", help="Video Edit/Extend source URL")
    generate.add_argument("--reference-images", nargs="*", help="Video Edit reference image URLs")
    generate.add_argument("--reference-audios", nargs="*", help="Video Edit reference audio URLs")
    generate.add_argument("--last-image", help="Video Extend target frame URL")
    generate.add_argument("--generate-audio", action="store_true", help="Generate audio for edit/extend")
    generate.add_argument("--no-audio", action="store_true", help="Preserve/omit source audio for edit/extend")
    generate.add_argument("--webhook-url", help="Optional completion webhook URL")
    add_video_options(generate)

    character = subparsers.add_parser("character", help="Create a character sheet")
    character.add_argument("--images", required=True, nargs="+", help="Reference images (1-3)")
    character.add_argument("--outfit", required=True, help="Outfit/style description")
    character.add_argument("--name", help="Character name")
    character.add_argument("--wait", action="store_true", help="Wait for completion")

    wm = subparsers.add_parser("watermark-remover", help="Remove a watermark")
    wm.add_argument("--video_url", required=True, help="Video URL")
    wm.add_argument("--wait", action="store_true", help="Wait for completion")

    wm_pro = subparsers.add_parser("watermark-remover-pro", help="Remove a watermark with Pro")
    wm_pro.add_argument("--video_url", required=True, help="Video URL")
    wm_pro.add_argument("--wait", action="store_true", help="Wait for completion")

    status = subparsers.add_parser("status", help="Get task status")
    status.add_argument("--request_id", required=True, help="Request ID")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    try:
        api = SeedanceAPI()

        if args.command == "t2v":
            result = api.text_to_video(
                args.prompt,
                args.aspect_ratio,
                args.duration,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "i2v":
            result = api.image_to_video(
                args.prompt,
                args.image_url,
                args.aspect_ratio,
                args.duration,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "first-last":
            result = api.first_last_frame(
                args.prompt,
                args.images,
                args.aspect_ratio,
                args.duration,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "omni":
            result = api.omni_reference(
                args.prompt,
                args.aspect_ratio,
                args.duration,
                args.images,
                args.videos,
                args.audios,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "edit":
            result = api.video_edit(
                args.prompt,
                args.video,
                args.reference_images,
                args.reference_audios,
                args.aspect_ratio,
                args.duration,
                not args.no_audio,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "extend":
            result = api.video_extend(
                args.prompt,
                args.video,
                args.last_image,
                args.aspect_ratio,
                args.duration,
                not args.no_audio,
                args.seed,
                args.variant,
                args.resolution,
            )
            print_result(api, result, args.wait)
        elif args.command == "generate":
            if args.generate_audio and args.no_audio:
                parser.error("--generate-audio and --no-audio cannot be used together")
            generate_audio = True if args.generate_audio else False if args.no_audio else None
            result = api.generate(
                endpoint=args.endpoint,
                prompt=args.prompt,
                aspect_ratio=args.aspect_ratio,
                duration=args.duration,
                seed=args.seed,
                image_url=args.image_url,
                images_list=args.images,
                videos_list=args.videos,
                audios_list=args.audios,
                video=args.video,
                reference_images=args.reference_images,
                reference_audios=args.reference_audios,
                last_image=args.last_image,
                generate_audio=generate_audio,
                webhook_url=args.webhook_url,
            )
            print_result(api, result, args.wait)
        elif args.command == "character":
            result = api.create_character(args.images, args.outfit, args.name)
            print_result(api, result, args.wait)
        elif args.command == "watermark-remover":
            result = api.watermark_remover(args.video_url)
            print_result(api, result, args.wait)
        elif args.command == "watermark-remover-pro":
            result = api.watermark_remover_pro(args.video_url)
            print_result(api, result, args.wait)
        elif args.command == "status":
            print(json.dumps(api.get_result(args.request_id), indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()

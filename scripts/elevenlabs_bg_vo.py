#!/usr/bin/env python3
"""
ElevenLabs Bulgarian TTS helper.

Usage:
    python3 scripts/elevenlabs_bg_vo.py \
        --text-file scripts/vo_bg_cb002.txt \
        --out build/vo_bg_cb002.mp3 \
        [--voice <voice_id>]

Requires:
    ELEVENLABS_API_KEY env var set.
    api.elevenlabs.io must be reachable from this environment
    (add to network allowlist if blocked).

Model: eleven_multilingual_v2 — supports Bulgarian (language_code: bg).
Default voice: "Aria" (multilingual female, warm tone — good for UGC skincare ads).
Override with --voice <voice_id> from ElevenLabs voice library.
"""
import argparse
import os
import sys
import requests

API_BASE = "https://api.elevenlabs.io"
DEFAULT_VOICE_ID = "9BWtsMINqrJLrRacOk9x"  # Aria — multilingual female
DEFAULT_MODEL = "eleven_multilingual_v2"


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs BG TTS")
    parser.add_argument("--text-file", required=True, help="Path to plain-text BG script")
    parser.add_argument("--out", required=True, help="Output MP3 path (e.g. build/vo_bg_cb002.mp3)")
    parser.add_argument("--voice", default=DEFAULT_VOICE_ID, help="ElevenLabs voice ID")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="ElevenLabs model ID")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY env var not set.", file=sys.stderr)
        sys.exit(1)

    with open(args.text_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    print(f"Generating BG TTS ({len(text)} chars) with voice {args.voice}...")

    url = f"{API_BASE}/v1/text-to-speech/{args.voice}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": text,
        "model_id": args.model,
        "language_code": "bg",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.2,
            "use_speaker_boost": True,
        },
        "output_format": "mp3_44100_128",
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        print(f"ERROR: ElevenLabs API returned {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(resp.content)

    print(f"Saved: {args.out} ({len(resp.content) / 1024:.1f} KB)")


if __name__ == "__main__":
    main()

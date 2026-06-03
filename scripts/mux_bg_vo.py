#!/usr/bin/env python3
"""
Mux a Bulgarian voiceover MP3 onto a silent (or muted) video.

Usage:
    python3 scripts/mux_bg_vo.py \
        --video build/assembled.mp4 \
        --audio build/vo_bg_cb002.mp3 \
        --out build/out_bg_cb002.mp4

Behaviour:
  - Replaces / overlays the audio track (video stream copied).
  - If VO is shorter than video: pads silence at end.
  - If VO is longer than video: trims to video duration.
  - Output is H.264 video + AAC 192k audio, 9:16 preserved.

Requires: imageio-ffmpeg (pip3 install imageio-ffmpeg) or system ffmpeg.
"""
import argparse
import subprocess
import sys
import os


def get_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return "ffmpeg"


def get_duration(ffmpeg_exe, path):
    result = subprocess.run(
        [ffmpeg_exe.replace("ffmpeg", "ffprobe") if "ffprobe" not in ffmpeg_exe else ffmpeg_exe,
         "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True, timeout=30
    )
    # fallback: use ffmpeg binary dir for ffprobe
    if result.returncode != 0:
        ffprobe = os.path.join(os.path.dirname(ffmpeg_exe), "ffprobe")
        if not os.path.exists(ffprobe):
            return None
        result = subprocess.run(
            [ffprobe, "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=30
        )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="Mux BG voiceover onto silent video")
    parser.add_argument("--video", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    ffmpeg = get_ffmpeg()
    ffprobe_dir = os.path.dirname(ffmpeg)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)

    vid_dur = get_duration(ffmpeg, args.video)
    aud_dur = get_duration(ffmpeg, args.audio)
    print(f"Video duration: {vid_dur:.2f}s  |  Audio duration: {aud_dur:.2f}s")

    if aud_dur is None or vid_dur is None:
        print("WARNING: Could not detect durations; using -shortest fallback.")
        cmd = [
            ffmpeg, "-y",
            "-i", args.video,
            "-i", args.audio,
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-map", "0:v:0", "-map", "1:a:0",
            "-shortest",
            args.out,
        ]
    elif aud_dur < vid_dur:
        # pad audio with silence to match video length
        print("Padding audio to match video length...")
        cmd = [
            ffmpeg, "-y",
            "-i", args.video,
            "-i", args.audio,
            "-filter_complex", "[1:a]apad[a]",
            "-map", "0:v:0", "-map", "[a]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            args.out,
        ]
    else:
        # trim audio to video duration
        print("Trimming audio to video duration...")
        cmd = [
            ffmpeg, "-y",
            "-i", args.video,
            "-i", args.audio,
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-map", "0:v:0", "-map", "1:a:0",
            "-t", str(vid_dur),
            args.out,
        ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.returncode != 0:
        print("ffmpeg stderr:", result.stderr[-2000:], file=sys.stderr)
        sys.exit(1)

    print(f"Done: {args.out}")
    final_dur = get_duration(ffmpeg, args.out)
    if final_dur:
        print(f"Output duration: {final_dur:.2f}s")
        if vid_dur and abs(final_dur - vid_dur) > 0.5:
            print(f"WARNING: duration mismatch > 0.5s (expected {vid_dur:.2f}s, got {final_dur:.2f}s)")


if __name__ == "__main__":
    main()

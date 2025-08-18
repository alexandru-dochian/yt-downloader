#!/usr/bin/env python3
import sys
import subprocess


def download_audio(url: str, output_dir: str = "./downloads"):
    try:
        cmd = [
            "yt-dlp",
            "--no-overwrites",
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            f"{output_dir}/%(title)s.%(ext)s",
            url,
        ]

        subprocess.run(cmd)
        print(f"Download complete. Files saved in: {output_dir}")

    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <video_or_playlist_url> [output_dir]")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./downloads"

    download_audio(url, output_dir)

# Youtube downloader

A simple Python script to download audio (MP3) from video or playlist URLs using `yt-dlp`.

## Features

- Downloads audio as MP3
- Skips existing files
- Works with both single videos and playlists

## Requirements

- [Python 3.12+](https://www.python.org/downloads/release/python-3120/)
- [Poetry](https://python-poetry.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Installation

Clone the repository:


```bash
git clone https://github.com/alexandru-dochian/yt-downloader 
cd yt-downloader
```

### **Install Poetry** (if not installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
poetry install
```

### Download

```bash
python3 main.py https://www.youtube.com/watch?v=2FRG4V7ZK5A
```


## Usage

*Usage: python3 main.py <video_or_playlist_url> [output_dir]*

- `<video_or_playlist_url>`: The URL of the video or playlist to download.
- `[output_dir]`: Optional directory to save downloaded files (default: `./downloads`).


## Notes

- Ensure `yt-dlp` is installed and accessible in your system PATH.
- Existing MP3 files in the output directory will be skipped.
- Works on Linux without modification.

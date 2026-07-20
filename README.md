# 🎥 YouTube Random Video Opener

A simple Python script that randomly opens YouTube videos from a predefined list and starts playback at a random timestamp.

## Features

* 🎲 Randomly selects a video from your collection
* ⏱️ Starts playback at a random timestamp
* 🌐 Opens videos in your default web browser
* 🔁 Repeats the process a configurable number of times
* 📦 Uses only Python's standard library (no external dependencies)

## Project Structure

```text
.
├── main.py
└── video_ids.py
```

The `video_ids.py` file should contain a dictionary in the following format:

```python
VIDEOS = {
    "VIDEO_ID_1": 180,
    "VIDEO_ID_2": 542,
    "VIDEO_ID_3": 97,
}
```

Where:

* **Key** - YouTube video ID
* **Value** - Video duration in seconds

## Requirements

* Python 3.8 or newer
* A default web browser

No additional packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/blockersiontko/deltarune_youtube_random_video_opener.git
cd deltarune_youtube_random_video_opener
```

## Usage

Run the script:

```bash
python main.py
```

By default, the script opens **50** randomly selected videos.

## Configuration

You can change the number of videos opened by modifying:

```python
TIMES = 50
```

You can also adjust the delay between openings:

```python
time.sleep(0.5)
```

## Example Output

```text
[1/50] Opening: https://youtu.be/dQw4w9WgXcQ?t=73
[2/50] Opening: https://youtu.be/abcdefghijk?t=215
[3/50] Opening: https://youtu.be/lmnopqrstuv?t=8
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**blocky**

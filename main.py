import webbrowser
import random
import time
from video_ids import VIDEOS

TIMES = 50

def get_url(video_id, start_time):
    return f"https://youtu.be/{video_id}?t={start_time}"

for i in range(TIMES):
    video_id = random.choice(list(VIDEOS.keys()))
    duration = VIDEOS[video_id]
    start_time = random.randint(0, max(duration - 5, 0))
    url = get_url(video_id, start_time)
    print(f"[{i+1}/{TIMES}] Opening: {url}")
    webbrowser.open(url)
    time.sleep(0.5)
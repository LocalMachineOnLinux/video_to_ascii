import moviepy.editor as ed
import os
import sys
import time
from numpy import arange
from PIL import Image
from frame import get_frame

def load_video():
    try:
        return ed.VideoFileClip(sys.argv[1])
    except IndexError:
        print("Please, use like this:")
        print("python main.py your_video.mp4")
        exit()

def make_terminal_clip(terminal_clip, length, fps):
    for frame_num in arange(0, length, 1/fps):
        clip_resized.save_frame("frame.jpg", t = frame_num)
        terminal_clip.append(get_frame(Image.open("frame.jpg")))
        os.remove("frame.jpg")
    return terminal_clip

def play_terminal_clip(terminal_clip, fps):
    for terminal_frame in terminal_clip:
        time.sleep(1/fps)
        print(terminal_frame)

if __name__ == '__main__':
    terminal_size = list(os.get_terminal_size())
    w, h = terminal_size

    clip = load_video()
    clip_resized = clip.resize(terminal_size)
    
    fps = clip_resized.fps
    duration = clip_resized.duration
    frames_nums = int(fps * duration)
    
    terminal_clip = make_terminal_clip([], duration, fps)

    try:
        if sys.argv[2] == "enable":
            import threading
            from playsound import playsound
            threading.Thread(target=playsound, args=(sys.argv[1],), daemon=True).start()
    except IndexError:
        pass
    play_terminal_clip(terminal_clip, fps)


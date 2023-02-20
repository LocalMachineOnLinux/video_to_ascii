import moviepy.editor as ed
import os
import sys
import time
import numpy as np
from PIL import Image
from frame import get_frame


class App():
    def __init__(self):
        self.terminal_size = list(os.get_terminal_size())
        self.width, self.height = self.terminal_size
        self.terminal_video = []

    def load_video(self):
        try:
            self.video = ed.VideoFileClip(sys.argv[1])
        except IndexError:
            print("Please, use like this:")
            print("python main.py your_video.mp4")
            exit()

    def resize_video(self):
        self.video = self.video.resize(self.terminal_size)
    
    def create_terminal_video(self):
        for frame_num in np.arange(0, self.video.duration, 1/self.video.fps):
            self.video.save_frame("frame.jpg", t = frame_num)
            frame = Image.open("frame.jpg")
            pixels = np.array(frame.getdata()).reshape(*frame.size, 3)
            self.terminal_video.append(get_frame(pixels, frame.size))
    
    def play_terminal_video(self):
        for terminal_frame in self.terminal_video:
            time.sleep(1/self.video.fps)
            print(terminal_frame)

    def run(self):
        self.load_video()
        self.resize_video()

        self.frames_nums = int(self.video.fps * self.video.duration)
        
        self.create_terminal_video()
        self.play_terminal_video()

if __name__ == '__main__':
    app = App()
    app.run()



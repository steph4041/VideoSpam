import numpy as np
import cv2
import random
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.playback import play
import threading

#config
y = 20 #numbers of windows the code will open
positions = [(random.randint(0, 1000), random.randint(0, 600)) for _ in range(y)] #coordinates for the opened windows
names = ['video.mp4'] * y #video name (caps sensitive)

#code
window_titles = [str(i) for i in range(y)]
cap = [cv2.VideoCapture(i) for i in names]
frames = [None] * len(names)
ret = [None] * len(names)
audio_clip = AudioSegment.from_file(names[0])
audio = 0
audio_clip = audio_clip.set_channels(1) 
audio_clip.export("temp_audio.wav", format="wav")
def play_audio():
    temp_audio = AudioSegment.from_wav("temp_audio.wav")
    play(temp_audio)
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()
while True:
    all_videos_ended = True
    for i, c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()
            if ret[i]:
                all_videos_ended = False
                cv2.imshow(window_titles[i], frames[i])
                cv2.moveWindow(window_titles[i], positions[i][0], positions[i][1])
    if all_videos_ended:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
for c in cap:
    if c is not None:
        c.release()
cv2.destroyAllWindows()

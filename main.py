import numpy as np
import cv2
import random
y = 100
positions = [(random.randint(0, 1000), random.randint(0, 600)) for _ in range(y)]

names = [];
window_titles = []
for n in range(y):
    names.append('video.mp4')
for n in range(y):
    window_titles.append(f'{n}')

cap = [cv2.VideoCapture(i) for i in names]

frames = [None] * len(names);
gray = [None] * len(names);
ret = [None] * len(names);

while True:

    for i, c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()

    for i, f in enumerate(frames):
        if ret[i] is True:
            cv2.imshow(window_titles[i], f)
            cv2.moveWindow(window_titles[i], positions[i][0], positions[i][1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


for c in cap:
    if c is not None:
        c.release();

cv2.destroyAllWindows()

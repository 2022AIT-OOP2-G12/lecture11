import pathlib
import cv2
import numpy as np

input_dir = "input_dir"
output_dir = "output_dir"
input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))

def mosaic(img, ratio=0.1):
    small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(img, x, y, width, height, ratio=0.1):
    dst = img.copy()
    dst[y:y+height, x:x+width] = mosaic(dst[y:y+height, x:x+width], ratio)
    return dst

cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

faces = cascade.detectMultiScale

if len(faces) > 0:
    for face in faces:
        x, y, w, h =face
        img_con = mosaic_area(img_con,x, y, w, h)

cv2.imwrite("mosaic_face.jpg", img_con)
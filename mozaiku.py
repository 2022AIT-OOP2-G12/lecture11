import pathlib
import cv2
import numpy as np

input_dir = "./static/input_dir"
output_dir = "./static/output_dir/mz/"
input_list = list(pathlib.Path(input_dir).glob('**/*.png'))

for i in range(len(input_list)):
    img_file_name = str(input_list[i])
    img = cv2.imread(img_file_name)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_con = img.copy()

    def mosaic(img, ratio=0.1):
        small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    def mosaic_area(img, x, y, width, height, ratio=0.1):
        dst = img.copy()
        dst[y:y+height, x:x+width] = mosaic(dst[y:y+height, x:x+width], ratio)
        return dst

    cascade = cv2.CascadeClassifier('./static/haarcascade_frontalface_alt2.xml')

    faces = cascade.detectMultiScale(img_gray)

    if len(faces) > 0:
        for face in faces:
            x, y, w, h =face
            img_con = mosaic_area(img_con,x, y, w, h)

    cv2.imwrite(f'{output_dir}{input_list[i].name}', img_con)
import pathlib
import cv2
import numpy as np

input_dir = "./static/input_dir"
output_dir = "./static/output_dir/gs/"
input_list = list(pathlib.Path(input_dir).glob('**/*.png'))

for i in range(len(input_list)):
    img_file_name = str(input_list[i])
    img_np = np.fromfile(img_file_name, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{output_dir}{input_list[i].name}', img_gray)
    
    
    
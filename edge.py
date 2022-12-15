import pathlib
import cv2
import numpy as np

input_dir = "input_dir"
output_dir = "output_dir"
input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))

for i in range(len(input_list)):
    img_file_name = str(input_list[i])
    img_np = np.fromfile(img_file_name, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cannyのエッジ検出
    canny_img  = cv2.Canny(img_gray,   # 入力画像
                       10, 
                       180  
                      )

    cv2.imwrite(f'./output_dir/{input_list[i].name}', canny_img)
    
    
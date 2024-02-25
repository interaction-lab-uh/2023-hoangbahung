import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
from PIL import Image
# パラメータの設定
_color ="GRAY" # RGB / GRAY
_average = "median" # mean / median
mv_file = "./ant_video/panic_2.mp4"
def cvt_color(img, color=_color):
    if color == "GRAY":
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        return img
# 出力先の設定
output = "./background/"
if not os.path.exists(output):
    os.mkdir(output)
#ビデオファイルの読み込みと各種設定の取得
video = cv2.VideoCapture(mv_file)
height, width, length = (
video.get(cv2.CAP_PROP_FRAME_HEIGHT),
video.get(cv2.CAP_PROP_FRAME_WIDTH),
video.get(cv2.CAP_PROP_FRAME_COUNT))
height, width = int(height), int(width)
# 下準備
if length >= 200:
    check_num = length // 100
    length = length // check_num
    length = 100
else :
    check_num = 1
    
if _color == "GRAY":
    data = np.empty((length, height, width), dtype="uint8")
else:
    data = np.empty((length, height, width, 3), dtype="uint8")
ret = True
frame_count = 0
data_index = 0
while ret:
    if data_index >= length:
        break
    ret, frame = video.read()
    if ret and frame_count%check_num==0:
        frame = cvt_color(frame)
        data[data_index] = frame
        data_index += 1
    frame_count += 1
if _average == "median":
    avarage_frame = np.median(data, axis=0).astype("uint8")
elif _average == "mean":
    avarage_frame = np.median(data, axis=0).astype("uint8")
name = mv_file.split(".")[:-1]
save = cv2.imwrite(output + ".".join(name) + "_" + _color + "_" + _average + ".jpg", avarage_frame)
if save:
    print("保存が完了しました")
else:
    print("error")
from PIL import Image
im = Image.fromarray(avarage_frame)
im.save("background.jpeg")
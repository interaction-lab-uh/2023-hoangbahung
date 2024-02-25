#import library + read file
import os
import pandas  as pd
width = 1080
height = 1920

data_path = "./ant_dataset/ant_anno.csv"
ant_data = pd.read_csv(data_path, header=1,usecols=[0,5], names = ["filename", "label"])
#データ中身確認
print(ant_data.head())
#ラベル確認＋処理
labels = []
string_labels = []
for i in range(len(ant_data["label"])):
    dict_data = eval(ant_data["label"][i])
    labels.append(list(dict_data.values()))
for i in range(len(labels)):
    labels[i][0] = 0
    labels[i][1] = labels[i][1]/width
    labels[i][2] = labels[i][2]/height
    labels[i][3] = labels[i][3]/width
    labels[i][4] = labels[i][4]/height

    string_labels_value = " ".join([str(item) for item in labels[i]])
    string_labels.append(string_labels_value)
#put data in txt file
i = 0
data = []
name = ant_data["filename"][0]

new_name = name.replace(".jpg", "")
for i in range(len(ant_data["filename"])):
    if ant_data["filename"][i] == name:
        data.append(string_labels[i])
    else:
        with open(f"./ant_dataset/labels/{new_name}.txt", 'w') as f:
            f.write('\n'.join(data))
        data.clear()
        name = ant_data["filename"][i]
        new_name = name.replace(".jpg", "")
# divide images and labels to train and valid data
import numpy as np
from sklearn.model_selection import train_test_split
import os

#get image's name from file
image_path = './ant_dataset/images/' 

file_names = os.listdir(image_path)

images = [file_name for file_name in file_names] 

#get label's name from file


label_path = './ant_dataset/labels/' 

label_names = os.listdir(label_path)

labels = [label_name for label_name in label_names] 

train_images, valid_images, train_labels, valid_labels = train_test_split(images, labels, test_size=0.3, random_state=42)
#put images and labels in train and val folder
import shutil
image_folder = "./ant_dataset/images"
label_folder = "./ant_dataset/labels"
image_train_folder = './ant_dataset/images/train'  
image_valid_folder = './ant_dataset/images/val' 
label_train_folder = './ant_dataset/labels/train'  
label_valid_folder = './ant_dataset/labels/val' 
os.makedirs(image_train_folder, exist_ok=True)
os.makedirs(image_valid_folder, exist_ok=True)
os.makedirs(label_train_folder, exist_ok=True)
os.makedirs(label_valid_folder, exist_ok=True)
for file in train_images:
    src_path = os.path.join(image_folder, file)
    dst_path = os.path.join(image_train_folder, file)
    shutil.move(src_path, dst_path)
for file in valid_images:
    src_path = os.path.join(image_folder, file)
    dst_path = os.path.join(image_valid_folder, file)
    shutil.move(src_path, dst_path)
for file in train_labels:
    src_path = os.path.join(label_folder, file)
    dst_path = os.path.join(label_train_folder, file)
    shutil.move(src_path, dst_path)
for file in valid_labels:
    src_path = os.path.join(label_folder, file)
    dst_path = os.path.join(label_valid_folder, file)
    shutil.move(src_path, dst_path)

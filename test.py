import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import pandas as pd
def read_train():
    train_path = '../dataset/images/train2017'
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
        images[n] = cv2.imread(os.path.join(mypath, onlyfiles[n]))
    return images
def read_val():
    val_path = "../dataset/images/val2017"
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
        images[n] = cv2.imread(os.path.join(mypath, onlyfiles[n]))
    return images
train=read_train()
val=read_val()

num=pd.read_csv("labels.csv")['num']
label=pd.read_csv("labels.csv")['label']
print(num)
print(label)




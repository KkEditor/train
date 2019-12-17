<<<<<<< HEAD
import tensorflow as tf
keras = tf.keras
K=keras.backend
def iou_coef(y_true, y_pred, smooth=1):
  intersection = K.sum(K.abs(y_true * y_pred), axis=[1,2,3])
  union = K.sum(y_true,[1,2,3])+K.sum(y_pred,[1,2,3])-intersection
  iou = K.mean((intersection + smooth) / (union + smooth), axis=0)
  return iou
=======
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import pandas as pd
from predict import Prediction
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
# train=read_train()
# val=read_val()
#
# num=pd.read_csv("labels.csv")['num']
# label=pd.read_csv("labels.csv")['label']
# print(num)
# print(label)
img=cv2.imread("1.jpeg",1)
img=cv2.resize(img,(256,256))
predictor = Prediction(model_weights_path='pretrained_deeplabv3.h5')
print(predictor.predict(img))

>>>>>>> 14e859e1ea6fa4341651434470c9d51baca7d435



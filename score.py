

import cv2
from model import Deeplabv3
import numpy as np

np.set_printoptions(precision=3)
img_size=512 #do Model pretrain tren dataset size 512
#--------------------------------------

image = cv2.imread("1.jpeg",1)
# np.set_printoptions(threshold=np.inf)  #option nhin duoc het cac sai so
weights='pascal_voc'                     #{'pascal_voc','cityscapes'}
input_tensor=None
input_shape=(img_size, img_size, 3)
classes=21
backbone='mobilenetv2'                   #{'xception','mobilenetv2'}
activation=None                          #{'softmax', 'sigmoid',None}
OS=16                                    #{8,16}
#---------------------------------------


resized_image = cv2.resize(image,(img_size,img_size))
# make prediction
deeplab_model = Deeplabv3(weights,input_tensor,input_shape,classes,backbone,activation,OS)
res = deeplab_model.predict(np.expand_dims(resized_image, 0))
res=res.squeeze()
print(res)

# labels = np.argmax(res, -1)
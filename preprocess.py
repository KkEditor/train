import os
import numpy as np
import cv2
import time

mean_subtraction_value=127.5
def resize(image):
  w, h, _ = image.shape
  ratio = float(trained_image_width) / np.max([w, h])
  resized_image = np.array(Image.fromarray(image.astype('uint8')).resize((int(ratio * h), int(ratio * w))))
  return resized_image


def normalize(img):
  img = (img / mean_subtraction_value) - 1
  return img


start_time = time.time()
mypath="./dataset/images/train2017"
edited="./dataset/images/editedtrain/"
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
i=0
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]))
  print("done "+str(i))
  res=resize(images[n])
  res=normalize(res)
  cv2.imwrite(edited+str(i)+'.jpg',res)
  i+=1
print("--- %s seconds ---" % (time.time() - start_time))

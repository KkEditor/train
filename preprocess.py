import os
import numpy as np
import cv2
import time
start_time = time.time()
mypath="./dataset/images/train2017"
edited="./dataset/images/editedtrain/"
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
i=0
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]))
  print("done "+str(i))
  cv2.imwrite(edited+str(i)+'.jpg',images[n])
  i+=1
print("--- %s seconds ---" % (time.time() - start_time))

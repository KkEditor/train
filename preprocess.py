import os
import numpy as np
import cv2
import time
start_time = time.time()
mypath='C:\\Users\\kk\\Desktop\\VOCtrainval_11-May-2012\\VOCdevkit\\VOC2012\\JPEGImages'
edited='C:\\Users\\kk\\Desktop\\'
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
i=0
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]))
  print("done "+str(i))
  cv2.imwrite('C:\\Users\\kk\\Desktop\\edited\\'+str(i)+'.jpeg',images[n])
  i+=1
print("--- %s seconds ---" % (time.time() - start_time))

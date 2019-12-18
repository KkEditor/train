import cv2
mypath="/image/"
edited="/mask/"
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
i=1
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]),cv2.IMREAD_UNCHANGED)
  cv2.imwrite(mypath+str(i)+".png",images[n])
  print("done " +str(i))
  # Alpha = images[n][:, :, 3]
  # cv2.imwrite(edited)


import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cv2
from model import Deeplabv3
from model import relu6

trained_image_width=512
mean_subtraction_value=127.5
def read_data():
    train_path = '../dataset/images/train2017'
    val_path = "../dataset/images/val2017"

image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# resize to max dimension of images from training dataset
w, h, _ = image.shape
ratio = float(trained_image_width) / np.max([w, h])
resized_image = np.array(Image.fromarray(image.astype('uint8')).resize((int(ratio * h), int(ratio * w))))

# apply normalization for trained dataset images
resized_image = (resized_image / mean_subtraction_value) - 1.

# pad array to square image to match training images
pad_x = int(trained_image_width - resized_image.shape[0])
pad_y = int(trained_image_width - resized_image.shape[1])
resized_image = np.pad(resized_image, ((0, pad_x), (0, pad_y), (0, 0)), mode='constant')


# deeplab_model=load_model('pretrained_deeplabv3.h5',custom_objects={'relu6':relu6})
deeplab_model = Deeplabv3()
res = deeplab_model.predict(np.expand_dims(resized_image, 0))
labels = np.argmax(res.squeeze(), -1)

# remove padding and resize back to original image
if pad_x > 0:
    labels = labels[:-pad_x]
if pad_y > 0:
    labels = labels[:, :-pad_y]
labels = np.array(Image.fromarray(labels.astype('uint8')).resize((h, w)))

plt.imshow(labels)
plt.waitforbuttonpress()

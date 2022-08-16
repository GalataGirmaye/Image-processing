from skimage.color import rgb2gray
from skimage.io import imread,imshow
import matplotlib.pyplot as plt

img = imread('./Images/lenna.jpeg')
img_new = rgb2gray(img)

plt.subplot(121), imshow(img)
plt.title('RGB Format') 

plt.subplot(122), imshow(img_new)
plt.title('HSV Format') 

plt.show()
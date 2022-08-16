import cv2
from matplotlib import pyplot as plt

img=cv2.imread('../Images/albert.jpeg',0)
img2=cv2.imread('../Images/lenna.jpeg',0)

img1_w,img1_h=img.shape
img2_w,img2_h=img2.shape
img = cv2.resize(img, img2.shape, interpolation = cv2.INTER_AREA)

print('Both shapes are:',img.shape,' and ',img2.shape)
sum=cv2.add(img,img2)

plt.imshow(sum,cmap='gray')
plt.show()
import cv2
import matplotlib.pyplot as plt

imgpath = "../Images/zebra.jpg"

gray = cv2.imread(imgpath, 0)
gray_negative = abs(255-gray)
imgs = [gray,gray_negative]
title = ['original', 'negative']


cv2.imwrite("../Images/zebra_negative.jpg",gray_negative)
plt.subplot(2, 2, 1)
plt.title(title[0])
plt.imshow(imgs[0],cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.title(title[1])
plt.imshow(imgs[1], cmap='gray')
plt.xticks([])
plt.yticks([])


plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:14:22 2022

@author: ai
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('../Images/albert.jpeg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #since cv2 loads in BGR format

# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)

# Display both images
# plt.imshow(image)
# plt.show()
# plt.imshow(log_image)
# plt.show()


plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(image)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.title('transformed')
plt.imshow(log_image, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../DATA/sammy_face.jpg')
# plt.imshow(img);
# plt.show()

"""
There is a lot of noise in the default
Can try to adjust thresholds
"""
# edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
# plt.imshow(edges);
# plt.show()


"""Alternative to creating better thresholds, doesnt always work well"""
# calculate median pixel value
med_val = np.median(img)
print(med_val)

# Set the lower threshold to zero or 70% of the median value, whichever is GREATER
lower = int(max(0,0.7*med_val))
# Upper threshold to either 130% of the median or the max of 255, whichever is SMALLER
upper = int(max(255,1.3*med_val))

# still not perfect, needs blurring
# edges = cv2.Canny(image=img, threshold1=lower, threshold2=upper)
# plt.imshow(edges);
# plt.show()

"""blurring the image will help the most"""
blurred_img = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(image=blurred_img, threshold1=lower, threshold2=upper)
plt.imshow(edges);
plt.show()

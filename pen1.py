import numpy as np
import imageio
import imageio.v2 as imageio
import scipy.ndimage
import cv2
img = "input.jpg"
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])
def dodge(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')
ss = imageio.imread(img)
gray = rgb2gray(ss)
cv2.imwrite('outputgray.png', gray)
i = 255-gray
blur = scipy.ndimage.gaussian_filter(i, sigma=13)
cv2.imwrite('outputblrred.png', blur) 
r = dodge(blur, gray)
cv2.imwrite('outputpencilsketch.png', r)
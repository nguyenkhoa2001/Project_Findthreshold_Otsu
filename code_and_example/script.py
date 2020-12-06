import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

im = cv2.imread("quarters_dimes_pennies.png", 0)

[hist, _] = np.histogram(im, bins=256, range=(0, 255)) 
val_max = 0
thr = 0
for t in range(1, 255):
    if ((np.sum(hist[t:]) == 0) or (np.sum(hist[:t]) == 0 )):
         continue
    P1 = np.sum(hist[t:]) / np.sum(hist)
    P2 = np.sum(hist[:t]) / np.sum(hist)
    A1 = np.sum(np.array([i for i in range(t, 256)]) * hist[t:]) / np.sum(hist[t:])
    A2 = np.sum(np.array([i for i in range(t)]) * hist[:t])/np.sum(hist[:t])
    val = P2 * P1 * np.power(A2-A1, 2)
    if val_max < val:
        val_max = val
        thr = t

print("Muc nguong T: {}".format(thr))

plt.subplot(121)
plt.imshow(im, cmap='gray')

im = im > thr
im = np.uint8(im)

plt.subplot(122)
plt.imshow(im, cmap='gray')

plt.show()
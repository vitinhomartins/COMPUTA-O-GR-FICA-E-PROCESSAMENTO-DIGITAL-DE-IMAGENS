import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("unequalized.jpg")

img = img.astype(np.float16)

c = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3

c = c.astype(np.uint8)

hist = np.zeros(256, dtype=int)

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        hist[c[i, j]] += 1


plt.bar(range(256), hist)

plt.title("Histograma - unequalized.jpg")
plt.xlabel("Nível de intensidade")
plt.ylabel("Quantidade de pixels")

plt.show()
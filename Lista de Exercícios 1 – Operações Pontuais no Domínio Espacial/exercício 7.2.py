import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(img):

    hist = np.zeros(256, dtype=int)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1

    return hist


img = cv2.imread("img_aluno.jpg")

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

hist_b = histograma(b)
hist_g = histograma(g)
hist_r = histograma(r)

plt.plot(hist_r, label="R")
plt.plot(hist_g, label="G")
plt.plot(hist_b, label="B")

plt.title("Histogramas RGB")
plt.xlabel("Nível de intensidade")
plt.ylabel("Quantidade de pixels")

plt.legend()
plt.show()
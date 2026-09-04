import cv2
import numpy as np
import matplotlib.pyplot as plt



def histograma(img):

    hist = np.zeros(256, dtype=int)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1

    return hist



def histograma_normalizado(img):

    hist = histograma(img)

    total_pixels = img.shape[0] * img.shape[1]

    hist_normalizado = hist / total_pixels

    return hist_normalizado



def histograma_acumulado(img):

    hist = histograma(img)

    acumulado = np.zeros(256, dtype=int)

    acumulado[0] = hist[0]

    for i in range(1, 256):
        acumulado[i] = acumulado[i - 1] + hist[i]

    return acumulado



def histograma_acumulado_normalizado(img):

    acumulado = histograma_acumulado(img)

    total_pixels = img.shape[0] * img.shape[1]

    acumulado_normalizado = acumulado / total_pixels

    return acumulado_normalizado



img = cv2.imread("unequalized.jpg")

# Converter para cinza
img = img.astype(np.float16)

c = (
    img[:, :, 0] +
    img[:, :, 1] +
    img[:, :, 2]
) / 3

c = c.astype(np.uint8)


# Histogramas

hist = histograma(c)

hist_norm = histograma_normalizado(c)

hist_acum = histograma_acumulado(c)

hist_acum_norm = histograma_acumulado_normalizado(c)



plt.figure()

plt.plot(hist_norm)

plt.title("Histograma Normalizado")

plt.xlabel("Intensidade")

plt.ylabel("Frequência")

plt.show()


plt.figure()

plt.plot(hist_acum)

plt.title("Histograma Acumulado")

plt.xlabel("Intensidade")

plt.ylabel("Quantidade acumulada")

plt.show()


plt.figure()

plt.plot(hist_acum_norm)

plt.title("Histograma Acumulado Normalizado")

plt.xlabel("Intensidade")

plt.ylabel("Frequência acumulada")

plt.show()
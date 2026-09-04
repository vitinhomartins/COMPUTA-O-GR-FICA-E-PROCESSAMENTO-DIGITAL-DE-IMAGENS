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



img = cv2.imread("img_aluno.jpg")



img = img.astype(np.float16)

c = (
    img[:, :, 0] +
    img[:, :, 1] +
    img[:, :, 2]
) / 3

c = c.astype(np.uint8)

cv2.imwrite("img_aluno_cinza.png", c)

cv2.imshow("Imagem em Cinza", c)

cv2.waitKey(0)
cv2.destroyAllWindows()


hist = histograma(c)

hist_norm = histograma_normalizado(c)

hist_acum = histograma_acumulado(c)

hist_acum_norm = histograma_acumulado_normalizado(c)



plt.plot(hist_norm)

plt.title("Histograma Normalizado - img_aluno")

plt.xlabel("Intensidade")

plt.ylabel("Frequência")

plt.show()


plt.plot(hist_acum)

plt.title("Histograma Acumulado - img_aluno")

plt.xlabel("Intensidade")

plt.ylabel("Quantidade acumulada")

plt.show()



plt.plot(hist_acum_norm)

plt.title("Histograma Acumulado Normalizado - img_aluno")

plt.xlabel("Intensidade")

plt.ylabel("Frequência acumulada")

plt.show()
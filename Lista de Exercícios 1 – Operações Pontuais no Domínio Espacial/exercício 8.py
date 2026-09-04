import cv2
import numpy as np
import matplotlib.pyplot as plt



def histograma(img):

    hist = np.zeros(256, dtype=int)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1

    return hist



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



def equalizacao(img):

    # Calcula o histograma acumulado normalizado
    acumulado_normalizado = histograma_acumulado_normalizado(img)

    # Cria a tabela de transformação
    tabela = (255 * acumulado_normalizado).astype(np.uint8)

    # Aplica a transformação
    resultado = tabela[img]

    return resultado



img = cv2.imread("unequalized.jpg")


img = img.astype(np.float16)

c = (
    img[:, :, 0] +
    img[:, :, 1] +
    img[:, :, 2]
) / 3

c = c.astype(np.uint8)


equalizada = equalizacao(c)



cv2.imshow("Original", c)

cv2.imshow("Equalizada", equalizada)

cv2.waitKey(0)

cv2.destroyAllWindows()


cv2.imwrite(
    "unequalized_equalizada.jpg",
    equalizada
)


hist_original = histograma(c)

plt.plot(hist_original)

plt.title("Histograma Original")

plt.xlabel("Intensidade")

plt.ylabel("Quantidade de pixels")

plt.show()



hist_equalizada = histograma(equalizada)

plt.plot(hist_equalizada)

plt.title("Histograma Equalizado")

plt.xlabel("Intensidade")

plt.ylabel("Quantidade de pixels")

plt.show()
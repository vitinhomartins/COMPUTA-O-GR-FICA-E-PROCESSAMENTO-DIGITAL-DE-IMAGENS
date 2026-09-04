import cv2
import numpy as np


def media_k_vizinhos(img, tamanho, k):

    resultado = np.zeros(img.shape, dtype=np.uint8)

    borda = tamanho // 2

    for i in range(borda, img.shape[0] - borda):
        for j in range(borda, img.shape[1] - borda):

            janela = img[
                i - borda:i + borda + 1,
                j - borda:j + borda + 1
            ]

            centro = img[i, j]

            valores = janela.flatten()

            distancias = np.abs(
                valores.astype(int) - int(centro)
            )

            indices = np.argsort(distancias)

            vizinhos = valores[indices[:k]]

            resultado[i, j] = np.mean(vizinhos)

    return resultado


img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

tamanho = 3
k = 5

resultado = media_k_vizinhos(img, tamanho, k)

cv2.imshow("Original", img)
cv2.imshow("Media dos k vizinhos", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img_aluno_media_k.jpg", resultado)
import cv2
import numpy as np


def mediana(img, tamanho):

    resultado = np.zeros(img.shape, dtype=np.uint8)

    borda = tamanho // 2

    for i in range(borda, img.shape[0] - borda):
        for j in range(borda, img.shape[1] - borda):

            janela = img[
                i - borda:i + borda + 1,
                j - borda:j + borda + 1
            ]

            valores = janela.flatten()

            resultado[i, j] = np.median(valores)

    return resultado


img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

tamanho = 3

resultado = mediana(img, tamanho)

cv2.imshow("Original", img)
cv2.imshow("Mediana", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img_aluno_mediana.jpg", resultado)
import cv2
import numpy as np


def media(img, tamanho):

    resultado = np.zeros(img.shape, dtype=np.uint8)

    borda = tamanho // 2

    for i in range(borda, img.shape[0] - borda):
        for j in range(borda, img.shape[1] - borda):

            janela = img[
                i - borda:i + borda + 1,
                j - borda:j + borda + 1
            ]

            resultado[i, j] = np.mean(janela)

    return resultado


img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

tamanho = 3

resultado = media(img, tamanho)

cv2.imshow("Original", img)
cv2.imshow("Media", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("lena_media.png", resultado)
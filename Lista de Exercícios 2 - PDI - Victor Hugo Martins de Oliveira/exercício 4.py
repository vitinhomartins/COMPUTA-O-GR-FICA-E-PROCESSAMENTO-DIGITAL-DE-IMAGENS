import cv2
import numpy as np


def laplaciano(img):

    resultado = np.zeros(img.shape, dtype=np.float32)

    mascara = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

            janela = img[i - 1:i + 2, j - 1:j + 2]

            resultado[i, j] = np.sum(janela * mascara)

    resultado = np.abs(resultado)

    resultado = np.clip(resultado, 0, 255)

    return resultado.astype(np.uint8)


img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

resultado = laplaciano(img)

cv2.imshow("Original", img)
cv2.imshow("Laplaciano", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img_aluno_laplacioano.jpg", resultado)
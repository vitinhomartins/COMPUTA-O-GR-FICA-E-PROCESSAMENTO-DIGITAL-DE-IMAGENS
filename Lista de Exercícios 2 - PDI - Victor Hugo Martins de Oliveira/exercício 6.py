import cv2
import numpy as np


def prewitt(img):

    resultado = np.zeros(img.shape, dtype=np.float32)

    mascara_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])

    mascara_y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ])

    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

            janela = img[i - 1:i + 2, j - 1:j + 2]

            gx = np.sum(janela * mascara_x)
            gy = np.sum(janela * mascara_y)

            resultado[i, j] = np.sqrt(gx ** 2 + gy ** 2)

    resultado = np.clip(resultado, 0, 255)

    return resultado.astype(np.uint8)


img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

resultado = prewitt(img)

cv2.imshow("Original", img)
cv2.imshow("Prewitt", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img_aluno_prewitt.jpg", resultado)
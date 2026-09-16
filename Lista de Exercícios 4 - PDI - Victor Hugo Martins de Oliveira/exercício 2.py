import cv2
import numpy as np

imagem = cv2.imread("pontos.png")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

filtro = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

resultado = cv2.filter2D(cinza, -1, filtro)

_, resultado = cv2.threshold(resultado, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("resultado_pontos.png", resultado)
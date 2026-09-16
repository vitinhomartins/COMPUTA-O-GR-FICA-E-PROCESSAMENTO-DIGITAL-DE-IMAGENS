import cv2
import numpy as np

imagem = cv2.imread("linhas.png")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

filtro_horizontal = np.array([
    [-1, -1, -1],
    [ 2,  2,  2],
    [-1, -1, -1]
])

filtro_vertical = np.array([
    [-1,  2, -1],
    [-1,  2, -1],
    [-1,  2, -1]
])

filtro_45 = np.array([
    [ 2, -1, -1],
    [-1,  2, -1],
    [-1, -1,  2]
])

filtro_menos45 = np.array([
    [-1, -1,  2],
    [-1,  2, -1],
    [ 2, -1, -1]
])

horizontal = cv2.filter2D(cinza, cv2.CV_32F, filtro_horizontal)
vertical = cv2.filter2D(cinza, cv2.CV_32F, filtro_vertical)
linha_45 = cv2.filter2D(cinza, cv2.CV_32F, filtro_45)
linha_menos45 = cv2.filter2D(cinza, cv2.CV_32F, filtro_menos45)

horizontal = cv2.convertScaleAbs(horizontal)
vertical = cv2.convertScaleAbs(vertical)
linha_45 = cv2.convertScaleAbs(linha_45)
linha_menos45 = cv2.convertScaleAbs(linha_menos45)

_, horizontal = cv2.threshold(horizontal, 100, 255, cv2.THRESH_BINARY)
_, vertical = cv2.threshold(vertical, 100, 255, cv2.THRESH_BINARY)
_, linha_45 = cv2.threshold(linha_45, 100, 255, cv2.THRESH_BINARY)
_, linha_menos45 = cv2.threshold(linha_menos45, 100, 255, cv2.THRESH_BINARY)

resultado = cv2.bitwise_or(horizontal, vertical)
resultado = cv2.bitwise_or(resultado, linha_45)
resultado = cv2.bitwise_or(resultado, linha_menos45)

cv2.imwrite("linha_horizontal.png", horizontal)
cv2.imwrite("linha_vertical.png", vertical)
cv2.imwrite("linha_45.png", linha_45)
cv2.imwrite("linha_menos45.png", linha_menos45)
cv2.imwrite("resultado_linhas.png", resultado)
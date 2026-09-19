import cv2
import numpy as np

imagem = cv2.imread("quadrados.png", cv2.IMREAD_GRAYSCALE)

elemento = np.ones((51, 51), np.uint8)

erosao = cv2.erode(imagem, elemento)

dilatacao = cv2.dilate(erosao, elemento)

cv2.imwrite("q2_erosao.png", erosao)
cv2.imwrite("q2_resultado.png", dilatacao)
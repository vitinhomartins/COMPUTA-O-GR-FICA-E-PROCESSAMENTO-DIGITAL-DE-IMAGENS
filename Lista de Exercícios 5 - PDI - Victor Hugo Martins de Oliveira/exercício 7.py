import cv2
import numpy as np

imagem = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

elemento = np.ones((3, 3), np.uint8)

dilatacao = cv2.dilate(imagem, elemento)

erosao = cv2.erode(imagem, elemento)

gradiente = cv2.subtract(dilatacao, erosao)

cv2.imwrite("q7_dilatacao.png", dilatacao)
cv2.imwrite("q7_erosao.png", erosao)
cv2.imwrite("q7_gradiente.png", gradiente)
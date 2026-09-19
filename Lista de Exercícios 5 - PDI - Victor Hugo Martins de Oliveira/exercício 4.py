import cv2
import numpy as np

imagem = cv2.imread("cachorro.png", cv2.IMREAD_GRAYSCALE)

elemento = np.ones((3, 3), np.uint8)

erosao = cv2.erode(imagem, elemento)
dilatacao = cv2.dilate(imagem, elemento)

borda_interna = cv2.subtract(imagem, erosao)
borda_externa = cv2.subtract(dilatacao, imagem)

cv2.imwrite("q4_borda_interna.png", borda_interna)
cv2.imwrite("q4_borda_externa.png", borda_externa)
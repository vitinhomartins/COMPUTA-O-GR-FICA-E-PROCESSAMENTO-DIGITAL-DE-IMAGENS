import cv2
import numpy as np

imagem = cv2.imread("ruidos.png", cv2.IMREAD_GRAYSCALE)

elemento = np.ones((3, 3), np.uint8)

def abertura(imagem, elemento):
    erosao = cv2.erode(imagem, elemento)
    resultado = cv2.dilate(erosao, elemento)
    return resultado

def fechamento(imagem, elemento):
    dilatacao = cv2.dilate(imagem, elemento)
    resultado = cv2.erode(dilatacao, elemento)
    return resultado

resultado_abertura = abertura(imagem, elemento)
resultado_fechamento = fechamento(imagem, elemento)

cv2.imwrite("q3_abertura.png", resultado_abertura)
cv2.imwrite("q3_fechamento.png", resultado_fechamento)
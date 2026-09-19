import cv2
import numpy as np
from collections import deque

imagem = cv2.imread("gato.png", cv2.IMREAD_GRAYSCALE)

_, bordas = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

altura, largura = bordas.shape

resultado = np.zeros_like(bordas)

semente_x = int(input("Digite X da semente: "))
semente_y = int(input("Digite Y da semente: "))

fila = deque()
fila.append((semente_y, semente_x))

visitados = np.zeros_like(bordas, dtype=np.uint8)

while fila:

    y, x = fila.popleft()

    if y < 0 or y >= altura or x < 0 or x >= largura:
        continue

    if visitados[y, x]:
        continue

    if bordas[y, x] != 0:
        continue

    visitados[y, x] = 1
    resultado[y, x] = 255

    fila.append((y - 1, x))
    fila.append((y + 1, x))
    fila.append((y, x - 1))
    fila.append((y, x + 1))

cv2.imwrite("q5_regiao_preenchida.png", resultado)
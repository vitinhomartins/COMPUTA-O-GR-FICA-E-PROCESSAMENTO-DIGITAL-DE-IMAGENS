import cv2
import numpy as np
from collections import deque

imagem = cv2.imread("quadrados.png", cv2.IMREAD_GRAYSCALE)

_, binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

altura, largura = binaria.shape

x = int(input("Digite X do ponto inicial: "))
y = int(input("Digite Y do ponto inicial: "))

componente = np.zeros_like(binaria)

fila = deque()
fila.append((y, x))

visitados = np.zeros_like(binaria, dtype=np.uint8)

while fila:

    cy, cx = fila.popleft()

    if cy < 0 or cy >= altura or cx < 0 or cx >= largura:
        continue

    if visitados[cy, cx]:
        continue

    visitados[cy, cx] = 1

    if binaria[cy, cx] == 0:
        continue

    componente[cy, cx] = 255

    fila.append((cy - 1, cx))
    fila.append((cy + 1, cx))
    fila.append((cy, cx - 1))
    fila.append((cy, cx + 1))

resultado = np.zeros((altura, largura, 3), dtype=np.uint8)

resultado[componente == 255] = (0, 255, 255)

cv2.imwrite("q6_componente_amarelo.png", resultado)
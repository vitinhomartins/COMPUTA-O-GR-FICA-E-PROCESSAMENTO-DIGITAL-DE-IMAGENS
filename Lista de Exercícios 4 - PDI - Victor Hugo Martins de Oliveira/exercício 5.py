import cv2
import numpy as np
from collections import deque

imagem = cv2.imread("root.jpg")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

semente_y = 115
semente_x = 347

limiar = 30

altura, largura = cinza.shape

resultado = np.zeros_like(cinza)
visitados = np.zeros_like(cinza, dtype=np.uint8)

fila = deque()
fila.append((semente_y, semente_x))

media_regiao = float(cinza[semente_y, semente_x])
quantidade = 1

vizinhos = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

while fila:
    y, x = fila.popleft()

    if y < 0 or y >= altura or x < 0 or x >= largura:
        continue

    if visitados[y, x]:
        continue

    visitados[y, x] = 1

    valor = float(cinza[y, x])

    if abs(valor - media_regiao) > limiar:
        continue

    resultado[y, x] = 255

    media_regiao = (media_regiao * quantidade + valor) / (quantidade + 1)
    quantidade += 1

    for dy, dx in vizinhos:
        fila.append((y + dy, x + dx))

cv2.imwrite("resultado_crescimento_regiao.png", resultado)
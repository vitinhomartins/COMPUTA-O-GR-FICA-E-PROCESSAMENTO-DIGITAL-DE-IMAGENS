import cv2
import numpy as np

def otsu(imagem):
    histograma = np.bincount(imagem.ravel(), minlength=256)
    total = imagem.size

    soma_total = np.sum(np.arange(256) * histograma)

    soma_fundo = 0
    peso_fundo = 0
    maior_variancia = 0
    melhor_limiar = 0

    for t in range(256):
        peso_fundo += histograma[t]

        if peso_fundo == 0:
            continue

        peso_objeto = total - peso_fundo

        if peso_objeto == 0:
            break

        soma_fundo += t * histograma[t]

        media_fundo = soma_fundo / peso_fundo
        media_objeto = (soma_total - soma_fundo) / peso_objeto

        variancia = peso_fundo * peso_objeto * (media_fundo - media_objeto) ** 2

        if variancia > maior_variancia:
            maior_variancia = variancia
            melhor_limiar = t

    _, resultado = cv2.threshold(
        imagem,
        melhor_limiar,
        255,
        cv2.THRESH_BINARY
    )

    return resultado


imagens = [
    "harewood.jpg",
    "nuts.jpg",
    "snow.jpg",
    "img_aluno.jpg"
]

for nome in imagens:
    imagem = cv2.imread(nome)

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    resultado = otsu(cinza)

    saida = "otsu_" + nome.rsplit(".", 1)[0] + ".png"

    cv2.imwrite(saida, resultado)
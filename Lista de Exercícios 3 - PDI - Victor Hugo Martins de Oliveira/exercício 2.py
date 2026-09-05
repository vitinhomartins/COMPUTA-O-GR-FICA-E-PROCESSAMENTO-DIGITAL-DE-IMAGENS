import cv2
import numpy as np
import matplotlib.pyplot as plt

def filtro_gaussiano(img, D0):
    f = np.fft.fft2(img)
    f = np.fft.fftshift(f)

    linhas, colunas = img.shape

    centro_x = linhas // 2
    centro_y = colunas // 2

    x = np.arange(linhas) - centro_x
    y = np.arange(colunas) - centro_y

    X, Y = np.meshgrid(y, x)

    D = np.sqrt(X ** 2 + Y ** 2)

    passa_baixa = np.exp(-(D ** 2) / (2 * D0 ** 2))
    passa_alta = 1 - passa_baixa

    resultado_baixa = f * passa_baixa
    resultado_alta = f * passa_alta

    resultado_baixa = np.fft.ifftshift(resultado_baixa)
    resultado_alta = np.fft.ifftshift(resultado_alta)

    resultado_baixa = np.fft.ifft2(resultado_baixa)
    resultado_alta = np.fft.ifft2(resultado_alta)

    resultado_baixa = np.abs(resultado_baixa)
    resultado_alta = np.abs(resultado_alta)

    resultado_baixa = cv2.normalize(
        resultado_baixa,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    resultado_alta = cv2.normalize(
        resultado_alta,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return resultado_baixa.astype(np.uint8), resultado_alta.astype(np.uint8)


nomes = [
    "teste.tif",
    "img_aluno.png"
]

for nome in nomes:
    img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Não foi possível abrir:", nome)
        continue

    passa_baixa, passa_alta = filtro_gaussiano(img, 30)

    cv2.imwrite(
        "passa_baixa_" + nome.split(".")[0] + ".png",
        passa_baixa
    )

    cv2.imwrite(
        "passa_alta_" + nome.split(".")[0] + ".png",
        passa_alta
    )

    plt.figure()
    plt.imshow(passa_baixa, cmap="gray")
    plt.title("Passa-baixa - " + nome)
    plt.axis("off")

    plt.figure()
    plt.imshow(passa_alta, cmap="gray")
    plt.title("Passa-alta - " + nome)
    plt.axis("off")

plt.show()
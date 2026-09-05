import cv2
import numpy as np
import matplotlib.pyplot as plt

def filtros_banda(img, D1, D2):
    f = np.fft.fft2(img)
    f = np.fft.fftshift(f)

    linhas, colunas = img.shape

    centro_x = linhas // 2
    centro_y = colunas // 2

    x = np.arange(linhas) - centro_x
    y = np.arange(colunas) - centro_y

    X, Y = np.meshgrid(y, x)

    D = np.sqrt(X ** 2 + Y ** 2)

    passa_banda = np.zeros(img.shape)

    passa_banda[(D >= D1) & (D <= D2)] = 1

    rejeita_banda = 1 - passa_banda

    resultado_banda = f * passa_banda
    resultado_rejeita = f * rejeita_banda

    resultado_banda = np.fft.ifftshift(resultado_banda)
    resultado_rejeita = np.fft.ifftshift(resultado_rejeita)

    resultado_banda = np.fft.ifft2(resultado_banda)
    resultado_rejeita = np.fft.ifft2(resultado_rejeita)

    resultado_banda = np.abs(resultado_banda)
    resultado_rejeita = np.abs(resultado_rejeita)

    resultado_banda = cv2.normalize(
        resultado_banda,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    resultado_rejeita = cv2.normalize(
        resultado_rejeita,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return passa_banda, rejeita_banda, resultado_banda.astype(np.uint8), resultado_rejeita.astype(np.uint8)


nomes = [
    "teste.tif",
    "img_aluno.jpg"
]

for nome in nomes:
    img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Não foi possível abrir:", nome)
        continue

    passa_banda, rejeita_banda, resultado_banda, resultado_rejeita = filtros_banda(img, 30, 80)

    cv2.imwrite(
        "passa_banda_" + nome.split(".")[0] + ".png",
        resultado_banda
    )

    cv2.imwrite(
        "rejeita_banda_" + nome.split(".")[0] + ".png",
        resultado_rejeita
    )

    plt.figure()
    plt.imshow(passa_banda, cmap="gray")
    plt.title("Filtro Passa-Banda")
    plt.axis("off")

    plt.figure()
    plt.imshow(rejeita_banda, cmap="gray")
    plt.title("Filtro Rejeita-Banda")
    plt.axis("off")

    plt.figure()
    plt.imshow(resultado_banda, cmap="gray")
    plt.title("Passa-Banda - " + nome)
    plt.axis("off")

    plt.figure()
    plt.imshow(resultado_rejeita, cmap="gray")
    plt.title("Rejeita-Banda - " + nome)
    plt.axis("off")

plt.show()
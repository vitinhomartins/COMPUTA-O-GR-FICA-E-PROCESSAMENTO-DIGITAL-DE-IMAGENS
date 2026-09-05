import cv2
import numpy as np
import matplotlib.pyplot as plt

def espectro_fourier(img):
    f = np.fft.fft2(img)
    f = np.fft.fftshift(f)

    espectro = np.log(1 + np.abs(f))

    espectro = cv2.normalize(
        espectro,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return espectro.astype(np.uint8)


nomes = [
    "arara.png",
    "barra1.png",
    "barra2.png",
    "barra3.png",
    "barra4.png",
    "teste.tif",
    "img_aluno.jpg"
]

for nome in nomes:
    img = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)

    resultado = espectro_fourier(img)

    plt.figure()
    plt.imshow(resultado, cmap="gray")
    plt.title(nome)
    plt.axis("off")

    cv2.imwrite("espectro_" + nome.split(".")[0] + ".png", resultado)

plt.show()
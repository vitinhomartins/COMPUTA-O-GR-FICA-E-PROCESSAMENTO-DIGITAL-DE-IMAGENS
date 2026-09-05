import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("arara.png", cv2.IMREAD_GRAYSCALE)
filtro = cv2.imread("arara_filtro.png", cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
f = np.fft.fftshift(f)

filtro = cv2.resize(filtro, (img.shape[1], img.shape[0]))

filtro = filtro / 255.0

resultado = f * filtro

resultado = np.fft.ifftshift(resultado)
resultado = np.fft.ifft2(resultado)

resultado = np.abs(resultado)

resultado = cv2.normalize(
    resultado,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

resultado = resultado.astype(np.uint8)

cv2.imshow("Arara", img)
cv2.imshow("Filtro", filtro)
cv2.imshow("Resultado", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("arara_rejeita_banda.png", resultado)

plt.figure()
plt.imshow(resultado, cmap="gray")
plt.title("Arara - Filtro Rejeita-Banda")
plt.axis("off")
plt.show()
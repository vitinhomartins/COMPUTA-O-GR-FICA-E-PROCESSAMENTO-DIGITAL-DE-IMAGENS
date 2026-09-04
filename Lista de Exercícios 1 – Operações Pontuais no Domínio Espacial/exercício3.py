import cv2
import numpy as np

img = cv2.imread("img_aluno.jpg")

img = img.astype(np.float16)

minimo = img.min()
maximo = img.max()

normalizada = ((img - minimo) / (maximo - minimo)) * 100

normalizada = normalizada.astype(np.uint8)


cv2.imshow("Imagem Normalizada", normalizada)

cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("normalizada.png", normalizada)
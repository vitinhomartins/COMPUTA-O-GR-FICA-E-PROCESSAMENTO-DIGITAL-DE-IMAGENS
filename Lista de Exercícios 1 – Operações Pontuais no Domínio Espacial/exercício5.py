import cv2
import numpy as np

img = cv2.imread("img_aluno.jpg")

img = img.astype(np.float32)

img = img / 255

potencia = 2 * (img ** 2)

potencia = potencia * 255

potencia = np.clip(potencia, 0, 255)

potencia = potencia.astype(np.uint8)

cv2.imshow("Operador de Potencia", potencia)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("potencia.png", potencia)
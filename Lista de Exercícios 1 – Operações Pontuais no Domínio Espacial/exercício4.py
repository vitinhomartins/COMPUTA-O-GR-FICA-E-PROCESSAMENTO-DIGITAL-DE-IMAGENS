import cv2
import numpy as np

img = cv2.imread("img_aluno.jpg")

img = img.astype(np.float32)

log = np.log(1 + img)

log = cv2.normalize(log, None, 0, 255, cv2.NORM_MINMAX)

log = log.astype(np.uint8)

cv2.imshow("Operador Logaritmico", log)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("logaritmico.png", log)
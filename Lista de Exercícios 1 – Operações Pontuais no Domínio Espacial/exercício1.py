import cv2
import numpy as np

img = cv2.imread("img_aluno.jpg")

img = img.astype(np.float16)

c = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3

c = c.astype(np.uint8)

cv2.imshow("Niveis de Cinza", c)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("cinza.png", c)
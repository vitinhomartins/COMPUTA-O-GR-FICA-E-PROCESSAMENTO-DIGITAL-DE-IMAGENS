import cv2
import numpy as np

img = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

for i in range(8):

    plano = ((img >> i) & 1) * 255

    plano = plano.astype(np.uint8)

    cv2.imshow(f"Bit {i + 1}", plano)

    cv2.imwrite(f"img_aluno(bit {i + 1}).png", plano)

cv2.waitKey(0)
cv2.destroyAllWindows()
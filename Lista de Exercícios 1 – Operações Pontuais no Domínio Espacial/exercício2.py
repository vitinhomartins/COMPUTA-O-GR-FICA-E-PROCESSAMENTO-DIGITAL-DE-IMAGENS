import cv2

img = cv2.imread("img_aluno.jpg")

negativo = 255 - img

cv2.imshow("Negativo", negativo)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite("negativo.png", negativo)
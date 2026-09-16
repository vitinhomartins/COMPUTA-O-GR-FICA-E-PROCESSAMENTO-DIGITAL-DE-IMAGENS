import cv2

imagem = cv2.imread("circuito.tif")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

resultado1 = cv2.medianBlur(cinza, 3)
resultado2 = cv2.medianBlur(resultado1, 3)
resultado3 = cv2.medianBlur(resultado2, 3)

cv2.imwrite("resultado_1.png", resultado1)
cv2.imwrite("resultado_2.png", resultado2)
cv2.imwrite("resultado_3.png", resultado3)
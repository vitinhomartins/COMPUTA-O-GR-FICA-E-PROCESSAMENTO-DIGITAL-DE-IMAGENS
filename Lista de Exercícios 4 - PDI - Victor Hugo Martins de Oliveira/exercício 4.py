import cv2

imagem = cv2.imread("igreja.png")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

resultado = cv2.Canny(cinza, 100, 200)

cv2.imwrite("resultado_canny.png", resultado)
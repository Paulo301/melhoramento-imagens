import cv2

img1 = cv2.imread("passaro.jpg")
img2 = cv2.imread("planeta.jpg")

image_add50 = cv2.add(img1, 50)
cv2.imshow("Adicao de escalar 50 na imagem 1", image_add50)

image_add = cv2.add(img1, img2)
cv2.imshow("Adicao de imagens", image_add)

image_sub50 = cv2.subtract(img1, 50)
cv2.imshow("Subtracao de escalar 50 na imagem 1", image_sub50)

image_sub = cv2.subtract(img1, img2)
cv2.imshow("Subtracao de imagens", image_sub)

image_mult = cv2.multiply(img1, 0.5)
cv2.imshow("Multiplicacao da imagem 1 por 0.5", image_mult)


cv2.waitKey(0)
cv2.destroyAllWindows()
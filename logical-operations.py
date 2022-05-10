import cv2

img1 = cv2.imread("passaro.jpg")
img2 = cv2.imread("planeta.jpg")

bitwise_not = cv2.bitwise_not(img2)
cv2.imshow("Operacao NOT", bitwise_not)

bitwise_or = cv2.bitwise_or(img2, img1)
cv2.imshow("Operacao OR", bitwise_or)

bitwise_and = cv2.bitwise_and(img2, img1)
cv2.imshow("Operacao AND", bitwise_and)

bitwise_xor = cv2.bitwise_xor(img2, img1)
cv2.imshow("Operacao XOR", bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
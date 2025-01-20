import cv2

img = cv2.imread(r'dragon.jpg', 0)
print(img)
status = cv2.imwrite('dragonbndw.png',img)
print("Image written to file-system: ", status)

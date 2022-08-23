#Exemplo de Algoritmo para codificar e decodificar imagens esteganográficas

import cv2
import numpy as np
import random
 
img1 = cv2.imread('config/cover_image.bmp')
img2 = cv2.imread('config/secret_image.bmp')

cv2.imshow("Cover_Image", img1) #cover_image
cv2.imshow("Secret_Image", img2) #secret_image
 
#encode image
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        for l in range(3):
            v1 = format(img1[i][j][l], '08b') #convert to bin
            v2 = format(img2[i][j][l], '08b')
            v3 = v1[:5] + v2[:3]              #sum bin images
            img1[i][j][l]= int(v3, 2)         #bin to int   
cv2.imshow("Hidden_Image", img1)

img = img1[:] #aux image
#set dimension
width = img.shape[0]
height = img.shape[1]
#create new images
img1 = np.zeros((width, height, 3), np.uint8)
img2 = np.zeros((width, height, 3), np.uint8)
 
#decode image
for i in range(width):
    for j in range(height):
        for l in range(3):#RGB channels
            v1 = format(img[i][j][l], '08b') #convert to bin
            v2 = v1[:3] + chr(random.randint(0, 1) + 48) * 3 #cover_image + 3 bits random noise
            v3 = v1[5:] + chr(random.randint(0, 1) + 48) * 5 #hidden_image + 5 bits noise
            #conver to img
            img1[i][j][l]= int(v2, 2)
            img2[i][j][l]= int(v3, 2)

cv2.imshow("Revealed_Cover_Image", img1)
cv2.imshow("Revealed_Secret_Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
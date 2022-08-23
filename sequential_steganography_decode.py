import cv2 as cv
import numpy as np 
import random 
from os import listdir, path
import time

def decodifica(img):
    new_img = img[:]
    w = img.shape[0]
    h = img.shape[1]

    img1 = np.zeros((w, h, 3), np.uint8)
    secret_image = np.zeros((w, h, 3), np.uint8)

    for i in range(w):
        for j in range(h):
            for k in range(3):
                v1 = format(new_img[i][j][k], '08b')
                v2 = v1[:3] + chr(random.randint(0, 1) + 48) * 3
                v3 = v1[5:] + chr(random.randint(0, 1) + 48) * 5
                img1[i][j][k] = int(v2, 2)
                secret_image[i][j][k] = int(v3, 2)

    return secret_image

if __name__ == "__main__":
    tempo_inicial = time.time()

    path = path.dirname(path.realpath(__file__)) + "/dataset_encoded"
    files = [f for f in listdir(path)]
    size_img = len(files)
    print("Total de imagens a serem decodificadas",size_img)

    for file in files:
        img = cv.imread(f'dataset_encoded/{file}')
        secret_image = decodifica(img)
        cv.imwrite(f"dataset_decoded/{file}", secret_image)
    tempo_exec = time.time() - tempo_inicial
    print (f"[SEQUENTIAL DECODED] Tempo de Execução: {round(tempo_exec)} segundos")
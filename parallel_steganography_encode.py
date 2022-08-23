import cv2 as cv
import numpy as np 
from os import listdir, path
import time
from joblib import Parallel, delayed

total_imagens = 0
def codifica(img):
    img = cv.imread(f'dataset/{file}')
    imagem_codificada = codifica(img)
    cv.imwrite(f"parallel_encoded/{file}", imagem_codificada)
    
    img1 = img
    secret_image = cv.imread('config/secret_image.bmp')
    w = secret_image.shape[0]
    h = secret_image.shape[1]

    for i in range(w):
        for j in range(h):
            for k in range(3):
                v1 = format(img1[i][j][k], '08b')
                v2 = format(secret_image[i][j][k], '08b')
                v3 = v1[:5] + v2[:3]
                img1[i][j][k] = int(v3,2)
    return img1

if __name__ == "__main__":
    tempo_inicial = time.time()
    path = path.dirname(path.realpath(__file__)) + "\dataset"
    files = [f for f in listdir(path)]
    Parallel(n_jobs = -1)(delayed(codifica)(file) for file in files)
    tempo_exec = time.time() - tempo_inicial
    print (f"[SEQUENTIAL ENCODED] Tempo de Execução: {round(tempo_exec)} segundos")
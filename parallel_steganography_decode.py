import multiprocessing
import threading
import cv2 as cv
import numpy as np 
import random 
from os import listdir, path
import os
import glob
import time
from joblib import Parallel, delayed

def decodifica(file):
    img = cv.imread(f'dataset_encoded/{file}')
    new_img = img[:]
    w = img.shape[0]
    h = img.shape[1]
    img1 = np.zeros((w, h, 3), np.uint8)
    img2 = np.zeros((w, h, 3), np.uint8)
    for i in range(w):
        for j in range(h):
            for k in range(3):
                v1 = format(new_img[i][j][k], '08b')
                v2 = v1[:3] + chr(random.randint(0, 1) + 48) * 3
                v3 = v1[5:] + chr(random.randint(0, 1) + 48) * 5
                img1[i][j][k] = int(v2, 2)
                img2[i][j][k] = int(v3, 2)
    cv.imwrite(f"dataset_decoded/{file}", img2)

def limpaDiretorio():
    bmp_files = glob.glob('dataset_decoded/*.bmp')
    for bmp_file in bmp_files:
        try:
            os.remove(bmp_file)
        except OSError as e:
            print(f"Error:{ e.strerror}")

if __name__ == "__main__":
    path = path.dirname(path.realpath(__file__)) + "/dataset_encoded"
    files = [f for f in listdir(path)]
    limpaDiretorio()
    tempo_inicial = time.time()
    Parallel(n_jobs = 1, backend=multiprocessing, batch_size=8)(delayed(decodifica)(file) for file in files)
    tempo_exec = time.time() - tempo_inicial
    print(f"[DECODIFICAÇÃO PARALELA] [Tempo de Execução: {round(tempo_exec)} s ]")

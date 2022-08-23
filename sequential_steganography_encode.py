import cv2 as cv
from os import listdir, path
import time

def codifica(cover_image):
    encode_image = cover_image
    secret_image = cv.imread('config/secret_image.bmp')
    w = secret_image.shape[0]
    h = secret_image.shape[1]

    for i in range(w):
        for j in range(h):
            for k in range(3):
                v1 = format(encode_image[i][j][k], '08b')
                v2 = format(secret_image[i][j][k], '08b')
                v3 = v1[:5] + v2[:3]
                encode_image[i][j][k] = int(v3,2)
    return encode_image

if __name__ == "__main__":
    tempo_inicial = time.time()

    path = path.dirname(path.realpath(__file__)) + "/dataset"
    files = [f for f in listdir(path)]
    size_img = len(files)
    print("Total de imagens a serem codificadas",size_img)

    for file in files:
        cover_image = cv.imread(f'dataset/{file}')
        imagem_codificada = codifica(cover_image)
        cv.imwrite(f"dataset_encoded/{file}", imagem_codificada)
    tempo_exec = time.time() - tempo_inicial
    print (f"[SEQUENTIAL ENCODED] Tempo de Execução: {round(tempo_exec)} segundos")

''' Curso IDASE
    Disciplina de Visão Computacional
    Doscente: Dr. Iago Zanuti Biundini
    Discente: Giovani Santiago Junqueira

    Aplicar os filtros de Borda e Suavização em um vídeo, em tempo real verificando a performance
    de cada um dos filtros. Aplicar o filtro de cor HSV em duas camadas ou seja, para duas cores.
'''

# Importação das Bibliotecas

import time
import cv2
import numpy as np


# Obtendo a imagem da webcam
# Indíce "0" - webcam do celular iPhone 13 (primeiro celular a vincular na minha conta Apple)
# Indíce "1" - webcam do celular iPhone 14 (segundo celular a vincular na minha conta Apple)
# Indíce "2" - webcam do macbook air (terceiro equipamento  a vincular na minha conta Apple)

webcam = cv2.VideoCapture(1)

# Verificando o tamanho da imagem
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = webcam.get(cv2.CAP_PROP_FPS)
print(f'Width: {width}, height: {height} e fps: {fps}')

# Estabelecendo os limites inferior e superior da cor Azul
hsv_low_b = np.array([89, 0, 0], np.uint8)
hsv_high_b = np.array([127, 255, 255], np.uint8)

# Estabelecendo os limites inferior e superior da cor Vermelho
hsv_low_r = np.array([0, 0, 0], np.uint8)
hsv_high_r = np.array([2, 255, 255], np.uint8)

while True:
    start_time = time.time()
    ret, frame = webcam.read()

    # Aplicação dos filtros de bordas.

    # Filtro de SOBEL
    sobelx = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=7)
    sobely = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=7)
    sobel2x = cv2.Sobel(frame, cv2.CV_8U, 0, 2, ksize=7)
    sobel2y = cv2.Sobel(frame, cv2.CV_8U, 2, 0, ksize=7)

    # Filtro Laplaciano
    lap = cv2.Laplacian(frame, cv2.CV_32F) #cv2.CV_8U

    # Filtro Canny
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 250)

    # Aplicação dos filtros de suavização

    # Filtro de Média
    media = cv2.blur(frame, (5, 5))

    # Filtro Gaussiano
    gaussian = cv2.GaussianBlur(frame, (5, 5), 0)

    # Filtro de Mediana
    median = cv2.medianBlur(frame, 5)

    # Aplicação da máscara de cores
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_blue = cv2.inRange(hsv, hsv_low_b, hsv_high_b)
    mask_red = cv2.inRange(hsv, hsv_low_r, hsv_high_r)
    mask_res = mask_blue + mask_red

    # Aplicação dos filtros HSV.

    # Filtro Azul
    f_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    # Filtro Vermelho
    f_red = cv2.bitwise_and(frame, frame, mask=mask_red)

    # Filtro combinado Azul e Vermelho
    res = cv2.bitwise_and(frame, frame, mask=mask_res)

    if ret:
        # Visualização da webcam Original, filtro de média, Gaussiano e Mediano
        cv2.imshow('Original / Media / Gaussiano / Mediana',
                   np.vstack([np.hstack([frame, media]), np.hstack([gaussian, median])]))

        # Visualização da webcam filtro SobelX, SobelY, Sobel2X e Sobel2Y
        cv2.imshow('Sobel X / Sobel Y / Sobel 2X / Sobel 2Y',
                   np.vstack([np.hstack([sobelx, sobely]), np.hstack([sobel2x, sobel2y])]))

        # Visualização da webcam filtro Laplaciano
        cv2.imshow('Laplacian', lap)

        # Visualização da webcam filtro Canny
        cv2.imshow('Canny', canny)

        # Visualização da webcam filtro HSV vermelho, HSV azul, HSV vermelhp e azul e original
        cv2.imshow('Vermelho / Azul / Resultado / Original',
                   np.vstack([np.hstack([f_blue, f_red]), np.hstack([res, frame])]))

        time.sleep(max(1./fps - time.time() - start_time,0))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# Ler imagem -> preparar máscaras -> procurar quadrados -> calcular poses dos quadrados

def encontra_quadrados(mascara):
    '''
        Encontra as posições dos quadrados na máscara

        Parâmetros:
            mascara: máscara que pode conter quadrados

        Retorna:
            quadrados: posições dos 4 vértices [[quad1],[quad2]]

    '''

    pass



img = cv.imread("img/frame0042.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

min_red = np.array([0,50,50])
max_red = np.array([10,255,255])

red_mask = cv.inRange(hsv, min_red, max_red)

min_green = np.array([55, 50, 50])
max_green = np.array([65, 255, 255])

green_mask = cv.inRange(hsv, min_green, max_green)

red_img = cv.bitwise_and(hsv,hsv, mask= red_mask)
green_img = cv.bitwise_and(hsv, hsv, mask=green_mask)

plt.imshow(cv.cvtColor(red_img,cv.COLOR_HSV2RGB))
plt.show()

plt.imshow(cv.cvtColor(green_img,cv.COLOR_HSV2RGB))
plt.show()

#red_bordas = cv.Canny(red_img, , )
#green_bordas = cv.Canny(green_img, , )




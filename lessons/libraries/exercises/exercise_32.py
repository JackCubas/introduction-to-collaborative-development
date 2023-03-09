import copy

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def coloursRed(imagen,i,j):
    imagen[i][j][1] = 0
    imagen[i][j][2] = 0

def coloursGreen(imagen,i,j):
    imagen[i][j][0] = 0
    imagen[i][j][2] = 0

def coloursBlue(imagen,i,j):
    imagen[i][j][0] = 0
    imagen[i][j][1] = 0

def splitter():

    redImg = sp.datasets.face().copy()
    greenImg = sp.datasets.face().copy()
    blueImg = sp.datasets.face().copy()
    for i in range(len(redImg)):
        for j in range(len(redImg[0])):
            coloursRed(redImg,i,j)
            coloursGreen(greenImg,i,j)
            coloursBlue(blueImg,i,j)
    colours = [redImg,greenImg,blueImg]
    return colours
foto = splitter()

plt.imshow(foto[0])
plt.show()
plt.imshow(foto[1])
plt.show()
plt.imshow(foto[2])
plt.show()

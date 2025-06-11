import numpy as np
from math import sqrt

def media_muestral_recursiva(media, valor, n_media):
    return media + (valor - media)/(n_media + 1)

def varianza_muestral_recursiva(varianza, media_vieja, media_nueva, n_varianza):
    termino_1 = (1- 1/n_varianza) * varianza
    termino_2 = (n_varianza + 1) * (media_nueva - media_vieja)**2
    return termino_1 + termino_2

def calcular_estimadores(N, d, random_func):
    media = random_func()
    Scuad, n = 0, 1 #Scuad = Sˆ2(1)
    while n<=N or sqrt(Scuad/n)>d:
        value = random_func()
        aux_media = media
        media = media_muestral_recursiva(media, value, n)
        Scuad = varianza_muestral_recursiva(Scuad, aux_media, media, n)
        n += 1
    return n, media, Scuad

def print_estimadores(N, media, Scuad):
    print(f"N: {N}")
    print(f"media muestral: {media}")
    print(f"varianza muestral: {Scuad}")
    return
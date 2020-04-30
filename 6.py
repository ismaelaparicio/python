# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:34:40 2020

@author: ismal
"""


abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto QUE QUIERES CIFRAR:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


texto_cifrado=""

for letra in texto_claro:
    nueva_posicion=(abecedario.index(letra)+clave) % 27
    letra_cifrada=abecedario[nueva_posicion]
    texto_cifrado+=letra_cifrada

print(texto_cifrado)
    
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:03:02 2020

@author: ismal
"""

print ("BIENVENIDO A EMPAREJANDO.COM")

nombre= input("Tu nombre:")
ano= int(input( "¿Año de nacimiento?" ))
tegusta= input("¿Te gusta taburete?")

edad  =  2020 - ano

print ("hola", nombre, ". Si no me equivoco tienes", edad, "años.")

if tegusta == "si" or tegusta == "Si":
  print('OK Boomer, lo tuyo va a ser un caso difícil.')
elif tegusta == "no" or tegusta == "No":
  print('Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.')

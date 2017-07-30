# -*- coding: utf-8 -*-
'''
Universidad del Valle de Guatemala
Métodos Numéricos 1 - Sección 51
Juan Andrés García - 15046
Laboratorio No. 2 - Programa principal
24/07/017
'''
# Importando modulos
from Lab2 import *
# Inicio del programa
print "Bienvenido al programa"
print "La funcion de prueba es: x^3 + 3x -1, puede cambiar la funcion en el modulo Lab2.py"
xl = float(raw_input("Ingrese el limite inferior: "))
xu = float(raw_input("Ingrese el limite superior: "))
er = float(raw_input("Ingrese su estimacion para el error: "))
miVariable = int(raw_input("Ingrese la forma de desplegar el resultado (1 o 2): "))
print "Metodo de biseccion:"
biseccion(xl,xu,er,miVariable)
print  "Metodo de falsa posicion:"
falsapos(xl,xu,er,miVariable)
fx = abs(f(xl))
print "Metodo de Newton-Raphson:"
newtonraphson(xl,fx,er,miVariable)

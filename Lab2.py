# -*- coding: utf-8 -*-
'''
Universidad del Valle de Guatemala
Métodos Numéricos 1 - Sección 51
Juan Andrés García - 15046
Laboratorio No. 2
24/07/017
'''
import math
# Funcion de prueba
def f(x):
    return 3*x + 7
# Metodo de biseccion
# Parametros: extremos del intervalo (xl, xu), error estimado (er) y forma de desplegar la respuesta (f)
def biseccion(xl,xu,er):
    xr = (xl + xu)/2.0
    iteraciones = 0
    while (xu-xl)/2.0 > er:
        if f(xr) == 0:
            return xr
        elif f(xl)*f(xr)<0:
            xu = xr
            iteraciones = iteraciones +1
        else:
            xl = xr
            iteraciones = iteraciones +1
        xr = (xl+xu)/2.0
    print "El cero estimado de la funcion es:",xr
    print "El numero de iteraciones fue:",iteraciones
# Metodo de falsa posicion
# Parametros: extremos del intervalo (xl, xu), error estimado (er) y forma de desplegar la respuesta (f)
def falsapos(xl,xu,er):
    xr = xl - f(xl)*((xu-xl)/(f(xu)-f(xl)))
    iteraciones = 0
    while (xu - xl) / 2.0 > er:
        if f(xr) == 0:
            return xr
        elif f(xl) * f(xr) < 0:
            xu = xr
            iteraciones = iteraciones + 1
        else:
            xl = xr
            iteraciones = iteraciones + 1
        xr = xl - f(xl)*((xu-xl)/(f(xu)-f(xl)))
    print "El cero estimado de la funcion es:", xr
    print "El numero de iteraciones fue:", iteraciones
falsapos(-5,5,0.0001)
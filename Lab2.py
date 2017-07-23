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
    return x**3 + 3*x - 1
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
    xr = (xl - f(xl)*((xu-xl)/(f(xu)-f(xl))))
    xl2 = 0
    xu2 = 0
    iteraciones = 0
    while xr > er:
        xl2 = xl
        xu2 = xu
        if f(xr) == 0:
            return xr
        elif f(xl) * f(xr) < 0:
            xu = xr
            iteraciones = iteraciones + 1
        else:
            xl = xr
            iteraciones = iteraciones + 1
        xr = (xl - f(xl)*((xu-xl)/(f(xu)-f(xl))))
        if xl2 == xl:
            break
        if xu2 == xu:
            break
    print "El cero estimado de la funcion es:", xr
    print "El numero de iteraciones fue:", iteraciones
falsapos(0.0,1.0,0.000001)

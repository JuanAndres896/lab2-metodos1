# -*- coding: utf-8 -*-
'''
Universidad del Valle de Guatemala
Métodos Numéricos 1 - Sección 51
Juan Andrés García - 15046
Laboratorio No. 2
24/07/017
'''
import math
from sympy import *
# Funcion de prueba
def f(x):
    return x**3 + 3*x - 1
# Funcion para calcular derivadas en un punto
def derivada(f,x):
    xi = float(x)
    try:
        y = eval(f)
        return y
    except:
        exit("Error")
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
        if f(xr) == 0:
            return xr
        elif f(xl) * f(xr) < 0:
            xu = xr
            iteraciones = iteraciones + 1
        else:
            xl = xr
            iteraciones = iteraciones + 1
        xr = (xl - f(xl)*((xu-xl)/(f(xu)-f(xl))))
        if xu2 == xu and xl2 == xl:
            break
        xl2 = xl
        xu2 = xu
    print "El cero estimado de la funcion es:", xr
    print "El numero de iteraciones fue:", iteraciones
# Metodo de Newton-Raphson
# Parametros: aproximacion inicial (x0), error estimado (er), iteraciones (n), forma de desplegar la respuesta (f)
def newtonraphson(x0,er,n):
    x0 = float(x0)
    resultados = [[0,x0,None]]
    x = symbols('x')
    ff = x**3 + 3*x -1
    fprima = diff(ff,"x")
    for i in range(1,n):
        try:
            xsuc = x0 - f(x0)/derivada(str(fprima),x0)
        except:
            print "Division entre cero, error."
            break
        ea = 100*(abs(xsuc-x0/xsuc))
        r = [i,xsuc,ea]
        resultados.append(r)
        x0 = xsuc
    return resultados
newtonraphson(1,0.00001,20)
# -*- coding: utf-8 -*-
'''
Universidad del Valle de Guatemala
Métodos Numéricos 1 - Sección 51
Juan Andrés García - 15046
Laboratorio No. 2
24/07/017
'''
# Funcion de prueba
def f(x):
    f = x**3 + 3*x - 1
    return f
# Funcion para calcular derivadas en un punto
def derivada(x,h):
    df = (f(x+h)-f(x))/h
    return df
# Metodo de biseccion
# Parametros: extremos del intervalo (xl, xu), error estimado (er) y forma de desplegar la respuesta (d)
def biseccion(xl,xu,er,d):
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
    if d == 2:
        print "El cero estimado de la funcion es:",xr
        print "El numero de iteraciones fue:",iteraciones
    elif d==1:
        print "El cero estimado de la funcion es:",xr
# Metodo de falsa posicion
# Parametros: extremos del intervalo (xl, xu), error estimado (er) y forma de desplegar la respuesta (d)
def falsapos(xl,xu,er,d):
    xr = xl - f(xl)*(xu-xl)/f(xu)-f(xl)
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
    if d==2:
        print "El cero estimado de la funcion es:", xr
        print "El numero de iteraciones fue:", iteraciones
    elif d==1:
        print "El cero estimado de la funcion es:",xr
# Metodo de Newton-Raphson
# Parametros: aproximacion inicial (x), imagen de la funcion (fx), error estimado(er) y forma de desplegar la respuesta (d)
def newtonraphson(x,fx,er,d):
    iteraciones = 0
    while fx > er:
        xi = x-f(x)/derivada(x,er)
        x = xi
        iteraciones = iteraciones+1
        fx = abs(f(x))
    if d==2:
        print "El cero estimado es:",x
        print "El numero de iteraciones fue:",iteraciones
    if d==1:
        print "El cero estimado es:",x
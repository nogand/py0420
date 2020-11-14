#!/usr/bin/env python
# -*- coding: utf-8 -*-

#funcion que me devuelve true si divisieble por cualquiera de los numero y falso si no lo es
def divisible(numero):
    if numero%2==0 or numero%3==0 or numero%5==0:
       return True
    else:
        return False

##Declaro e inicializo la lista
lista=[]
for i in range(1,101):
    lista.append(i)

#recorro la lista y llamo a la funcion divisible por cada numero

for numero in lista:
    if divisible(numero):
        print (numero,"\t divisible")
    else:
        print(numero)
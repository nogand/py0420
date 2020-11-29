#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def cargar(archivo="paises.json"):
  fentrada = open(archivo)
  datos = json.load(fentrada)
  fentrada.close()
  return datos

def guardar(datos, archivo="paises.json"):
  with open(archivo, "w") as fsalida:
    fsalida.write(json.dumps(datos))

if __name__ == '__main__':
  import sys
  print ("Esto es un módulo. No se ejecuta de manera directa.", file=sys.stderr)

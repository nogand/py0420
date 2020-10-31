#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import archivo_v2 as archivo
paises={}

if (len(sys.argv)>3 or len(sys.argv)<2):
  print("""Error de llamada.
Este programa debe ser invocado:
guardar.py <archivo de entrada> [<archivo de salida>]
""",file=sys.stderr)
  exit(1)

if len(sys.argv) == 3 :
  asalida=sys.argv[2]
else :
  asalida="paises.json"

with open(sys.argv[1]) as aentrada:
  for pais in aentrada:
    (pais, capital, lider)=pais.split(",")
    paises[pais]={"capital": capital, "lider": lider.strip()}

archivo.guardar(paises, asalida)

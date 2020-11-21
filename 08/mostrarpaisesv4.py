#!/usr/bin/env python
# -*- coding: utf-8 -*-
import archivo_v3 as archivo

with open("paises.csv") as aentrada:
  for pais in aentrada:
    (pais, capital, lider)=pais.split(",")
    print("El pais {} con capital en {} es liderado por {}".format(pais,capital,lider.strip()))

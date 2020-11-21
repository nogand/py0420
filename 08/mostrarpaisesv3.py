#!/usr/bin/env python
# -*- coding: utf-8 -*-
import archivo_v3 as archivo

with open("paises.csv") as aentrada:
  for pais in aentrada:
    listap=pais.split(",")
    print("El pais {} con capital en {} es liderado por {}".format(listap))

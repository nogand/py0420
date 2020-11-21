#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import archivo_v3 as archivo
import sqlite3

if (len(sys.argv)!=2):
  print("""Error de llamada.
Este programa debe ser invocado:
{} <archivo de entrada>
""".format(sys.argv[0]),file=sys.stderr,end="")
  exit(1)

cnx=sqlite3.connect("paises.db")
cur=cnx.cursor()

cur.execute("CREATE TABLE if not exists pais (nombre text PRIMARY KEY, capital text, lider text)")
cnx.commit()

with open(sys.argv[1]) as aentrada:
  for pais in aentrada:
    datos=pais.split(",")
    datos[2]=datos[2].strip()
    cur.execute("INSERT INTO pais VALUES (?,?,?)",datos)
cnx.commit()
cnx.close()

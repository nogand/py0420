#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os
import psycopg2
import sys

# Cargamos el archivo de configuración y las variables relevantes
ACONFIG=os.getenv('ACONFIG', '../configuracion/paises.ini')
config=configparser.ConfigParser()
config.read(ACONFIG)
USUARIO_BDD=os.getenv('USUARIO_BDD', config['BDD'].get('usuario'))
CLAVE_BDD=os.getenv('CLAVE_BDD', config['BDD'].get('clave'))
SERVIDOR_BDD=os.getenv('SERVIDOR_BDD', config['BDD'].get('servidor'))
NOMBRE_BDD=os.getenv('NOMBRE_BDD', config['BDD'].get('nombre'))

cnx=psycopg2.connect(dbname=NOMBRE_BDD, user=USUARIO_BDD, host=SERVIDOR_BDD, password=CLAVE_BDD)
cur=cnx.cursor()

# Recibimos el parámetro del usuario
ID_CIUDAD=sys.argv[1]

cur.execute("SELECT id, nombre, pais, capital FROM ciudad WHERE id=%s;", (ID_CIUDAD,))
(id, nombre, pais, capital) = cur.fetchone()
print(id,nombre,pais,capital,sep="\t")
cnx.close()

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

# Recibimos los parámetros del usuario
ID_PAIS=sys.argv[1]
ID_LIDER=sys.argv[2]
TITULO_LIDER=sys.argv[3]
FECHA_INICIO=sys.argv[4]
if len(sys.argv)==6 :
    FECHA_FINAL=None
    ES_PRINCIPAL=sys.argv[5]
else :
    FECHA_FINAL=sys.argv[5]
    ES_PRINCIPAL=sys.argv[6]

cur.execute("INSERT INTO lider_pais (pais, lider, titulo, fecha_inicio, fecha_final, principal) VALUES (%s, %s, %s, %s, %s, %s);", (ID_PAIS, ID_LIDER, TITULO_LIDER, FECHA_INICIO, FECHA_FINAL, (ES_PRINCIPAL=="1" or ES_PRINCIPAL=="Sí" or ES_PRINCIPAL=="Si" or ES_PRINCIPAL=="sí" or ES_PRINCIPAL=="si")))
cnx.commit()
cnx.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from flask_api import status
import configparser
import psycopg2
import os

app = Flask(__name__)


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

# Endpoints

@app.route("/pais/",methods=['GET'])
def mostrar_paises():
  cur.execute("SELECT id, nombre, cod_iso FROM pais;")
  listapaises=[]
  for (id, nombre, cod_iso) in cur.fetchall():
    listapaises.append({"id": id, "nombre": nombre, "cod_iso": cod_iso})
  return jsonify(listapaises), status.HTTP_200_OK

@app.route("/pais/",methods=['POST'])
def agregar_paises():
  datos = request.get_json()
  print(datos)
  try:
    cur.execute("INSERT INTO pais (nombre, cod_iso) VALUES (%s, %s);",(datos["nombre"], datos["cod_iso"]))
    cur.execute("SELECT currval('pais_id_seq')")
    (id,) = cur.fetchone()
    cnx.commit()
    return jsonify({"id": id}), status.HTTP_201_CREATED
  except psycopg2.errors.UniqueViolation as e:
    print("Error de llave duplicada:\n{}\n{}".format(type(e),str(e)))
    cnx.rollback()
    return jsonify({}), status.HTTP_409_CONFLICT
  except Exception as e:
    print("Excepción encontrada:\n{}\n{}".format(type(e),str(e)))
    cnx.rollback()
    return jsonify({}), status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route("/pais/<string:id>/",methods=['GET'])
def mostrar_pais(id):
  cur.execute("SELECT id, nombre, cod_iso FROM pais WHERE id=%s;", (id,))
  try :
    (id, nombre, cod_iso) = cur.fetchone()
    return jsonify({"id": id, "nombre": nombre, "cod_iso": cod_iso}), status.HTTP_200_OK
  except :
    return jsonify({}), status.HTTP_404_NOT_FOUND

@app.route("/pais/<string:id>/lider/",methods=['GET'])
def mostrar_pais_lider(id):
  cur.execute("SELECT pais, lider, titulo, fecha_inicio, fecha_final, principal is true FROM lider_pais WHERE pais=%s;", (id,))
  listaliderpaises=[]
  for (pais, lider, titulo, fecha_inicio, fecha_final, principal) in cur.fetchall():
    listaliderpaises.append({"pais": pais, "lider": lider, "titulo": titulo, "fecha_inicio": fecha_inicio, "fecha_final": fecha_final, "principal": principal})
  return jsonify(listaliderpaises), status.HTTP_200_OK

@app.route("/pais/<string:id>/ciudad/",methods=['GET'])
def mostrar_pais_ciudad(id):
  cur.execute("SELECT ciudad.id, ciudad.nombre, ciudad.pais, ciudad.capital is true FROM ciudad WHERE pais=%s;", (id,))
  listaciudadespais=[]
  for (id, nombre, pais, capital) in cur.fetchall():
    listaciudadespais.append({"id": id, "nombre": nombre, "pais": pais, "capital": capital})
  return jsonify(listaciudadespais), status.HTTP_200_OK

@app.route("/lider/",methods=['GET'])
def mostrar_lideres():
  cur.execute("SELECT id, nombre FROM lider;")
  listalideres=[]
  for (id, nombre) in cur.fetchall():
    listalideres.append({"id": id, "nombre": nombre})
  return jsonify(listalideres), status.HTTP_200_OK

@app.route("/lider/<string:id>/",methods=['GET'])
def mostrar_lider(id):
  cur.execute("SELECT id, nombre FROM lider WHERE id=%s;", (id,))
  try :
    (id, nombre) = cur.fetchone()
    return jsonify({"id": id, "nombre": nombre}), status.HTTP_200_OK
  except :
    return jsonify({}), status.HTTP_404_NOT_FOUND

@app.route("/lider/<string:id>/pais/",methods=['GET'])
def mostrar_lider_pais(id):
  cur.execute("SELECT pais, lider, titulo, fecha_inicio, fecha_final, principal is true FROM lider_pais WHERE lider=%s;", (id,))
  listaliderpaises=[]
  for (pais, lider, titulo, fecha_inicio, fecha_final, principal) in cur.fetchall():
    listaliderpaises.append({"pais": pais, "lider": lider, "titulo": titulo, "fecha_inicio": fecha_inicio, "fecha_final": fecha_final, "principal": principal})
  return jsonify(listaliderpaises), status.HTTP_200_OK

@app.route("/ciudad/",methods=['GET'])
def mostrar_ciudades():
  cur.execute("SELECT id, nombre, pais, capital is true FROM ciudad;")
  listaciudades=[]
  for (id, nombre, pais, capital) in cur.fetchall():
    listaciudades.append({"id": id, "nombre": nombre, "pais": pais, "capital": capital})
  return jsonify(listaciudades), status.HTTP_200_OK

@app.route("/ciudad/",methods=['POST'])
def agregar_ciudades():
  datos = request.get_json()
  try:
    cur.execute("INSERT INTO ciudad (nombre, pais, capital) VALUES (%s, %s, %s);",(datos["nombre"], datos["pais"], datos["capital"] is True))
    cur.execute("SELECT currval('ciudad_id_seq')")
    (id,) = cur.fetchone()
    return jsonify({"id": id}), status.HTTP_201_CREATED
  except Exception as e:
    print("Excepción encontrada:\n{}\n{}".format(type(e),str(e)))
    return jsonify({}), status.HTTP_500_INTERNAL_SERVER_ERROR


@app.route("/ciudad/<string:id>/",methods=['GET'])
def mostrar_ciudad(id):
  cur.execute("SELECT id, nombre, pais, capital is true FROM ciudad WHERE id=%s;", (id,))
  try :
    (id, nombre, pais, capital) = cur.fetchone()
    return jsonify({"id": id, "nombre": nombre, "pais": pais, "capital": capital}), status.HTTP_200_OK
  except :
    return jsonify({}), status.HTTP_404_NOT_FOUND

@app.route("/lider-pais/",methods=['GET'])
def mostrar_liderpaises():
  cur.execute("SELECT pais, lider, titulo, fecha_inicio, fecha_final, principal is true FROM lider_pais;")
  listaliderpaises=[]
  for (pais, lider, titulo, fecha_inicio, fecha_final, principal) in cur.fetchall():
    listaliderpaises.append({"pais": pais, "lider": lider, "titulo": titulo, "fecha_inicio": fecha_inicio, "fecha_final": fecha_final, "principal": principal})
  return jsonify(listaliderpaises), status.HTTP_200_OK

@app.route("/lider/<string:id_lider>/pais/<string:id_pais>",methods=['GET'])
@app.route("/pais/<string:id_pais>/lider/<string:id_lider>",methods=['GET'])
def mostrar_liderpais(id_lider, id_pais):
  cur.execute("SELECT pais, lider, titulo, fecha_inicio, fecha_final, principal is true FROM lider_pais WHERE lider=%s AND pais=%s;", (id_lider,id_pais))
  try :
    (pais, lider, titulo, fecha_inicio, fecha_final, principal) = cur.fetchone()
    return jsonify({"pais": pais, "lider": lider, "titulo": titulo, "fecha_inicio": fecha_inicio, "fecha_final": fecha_final, "principal": principal}), status.HTTP_200_OK
  except :
    return jsonify({}), status.HTTP_404_NOT_FOUND

if __name__ == '__main__':
  app.run(host='0.0.0.0')

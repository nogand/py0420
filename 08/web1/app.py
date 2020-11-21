#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

import archivo_v3 as archivo

@app.route('/hello')
def hello():
    return "Hello World!"

posts = []
@app.route("/")
def index():
    # return "{} posts".format(len(posts))
    return render_template("index.html", num_posts=len(posts))

@app.route("/p/<string:nombre>/")
def show_post(nombre):
    return "Mostrando el post {}".format(nombre)

@app.route("/paisviejo/<string:id>/")
def show_pais(id):
    mensaje="<H1>Mostrando el pais {}</H1>".format(id)
    with open("paises.csv") as aentrada:
        for pais in aentrada:
            (pais, capital, lider)=pais.split(",")
            if pais == id :
                mensaje+="El pais <B>{}</B> con capital en <B>{}</B> es liderado por <U>{}</U>.".format(pais,capital,lider.strip())
    return mensaje

@app.route("/pais/<string:id>/")
def mostrar_pais(id):
    with open("paises.csv") as aentrada:
        for pais in aentrada:
            (pais, capital, lider)=pais.split(",")
            # print("Voy por: {}".format(pais))
            if pais == id :
                return render_template("pais.html", pais=pais, capital=capital, lider=lider.strip())
    # print("Voy por el final...")
    return render_template("noexiste.html")

if __name__ == '__main__':
    app.run()

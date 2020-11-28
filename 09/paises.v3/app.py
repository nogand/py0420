#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import archivo_paises as ap
app = Flask(__name__)

paises = ap.cargar()

@app.route("/")
def index():
    # return "{} paises".format(len(paises))
    return render_template("index.html", num_paises=len(paises), paises=paises)

@app.route("/pais/<string:id>/")
def mostrar_pais(id):
    if id in paises :
        return render_template("pais.html", pais=id, capital=paises[id]["capital"], lider=paises[id]["lider"])
    return render_template("noexiste.html")

if __name__ == '__main__':
    app.run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return """
<H1>Hello World!</H1>
<HR>
<TABLE border=2>
    <TR>
        <TD>País</TD>
        <TD>Capital</TD>
        <TD>Líder</TD>
    </TR>
    <TR>
        <TD>Costa Rica</TD>
        <TD>San José</TD>
        <TD>Carlos Alvarado</TD>
    </TR>
</TABLE>
"""

if __name__ == '__main__':
    app.run()

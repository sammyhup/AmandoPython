from flask import Flask, g
import sqlite3

DATABASE = "blog.bd"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def fim_requisicao(exc):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    return str(entradas)
    
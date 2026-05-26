# database/conexao.py
import mysql.connector

DB_NAME = "firecommand"


def obter_conexao():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # ajusta se tiveres outro utilizador
        password="SUA_SENHA",  # mete aqui a tua password
        database=DB_NAME,
    )
    return conn

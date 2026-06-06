# database/conexao.py
import mysql.connector
from config import DB_CONFIG

def obter_conexao():
    """
    Cria e devolve uma conexão com a base de dados MySQL
    utilizando as configurações centralizadas no config.py.
    """
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )
    return conn
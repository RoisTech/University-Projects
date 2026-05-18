import mysql.connector
from config import DB_CONFIG


def ligar_bd():

    try:

        conexao = mysql.connector.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

        print("✅ Base de dados ligada.")

        return conexao

    except Exception as erro:

        print(f"❌ Erro MySQL: {erro}")

        return None
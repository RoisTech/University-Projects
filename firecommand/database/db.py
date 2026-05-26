# database/db.py
from database.conexao import obter_conexao


def iniciar_bd():
    conn = obter_conexao()
    cursor = conn.cursor()

    # Exemplo: criar uma tabela de teste (ajusta para o teu modelo real)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exemplo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

from database.conexao import obter_conexao

def iniciar_bd():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exemplo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    iniciar_bd()
    # resto do teu código (menu, GUI, etc.)

if __name__ == "__main__":
    main()
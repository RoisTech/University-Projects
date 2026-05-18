from database.db import ligar_bd


def criar_tabelas():

    conexao = ligar_bd()

    if not conexao:
        return

    cursor = conexao.cursor()

    # ====================================
    # UTILIZADORES
    # ====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilizadores (

        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        username VARCHAR(50) UNIQUE,
        password VARCHAR(255),
        tipo VARCHAR(50)

    )
    """)

    # ====================================
    # QUARTÉIS
    # ====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quarteis (

        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        tipo VARCHAR(50),
        distrito VARCHAR(50),
        latitude DOUBLE,
        longitude DOUBLE

    )
    """)

    # ====================================
    # OCORRÊNCIAS
    # ====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ocorrencias (

        id INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(100),
        severidade VARCHAR(50),
        vitimas INT,
        descricao TEXT,
        latitude DOUBLE,
        longitude DOUBLE,
        estado VARCHAR(50),
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # ====================================
    # DESPACHOS
    # ====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS despachos (

        id INT AUTO_INCREMENT PRIMARY KEY,
        quartel_id INT,
        ocorrencia_id INT,
        viatura VARCHAR(100),
        bombeiros INT,
        estado VARCHAR(50),
        hora_saida TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conexao.commit()

    print("✅ Tabelas criadas com sucesso.")

    cursor.close()
    conexao.close()


if __name__ == "__main__":
    criar_tabelas()
# database/db.py
import os
import mysql.connector
import csv  # Cumpre o requisito estrito de ficheiros do enunciado
from database.conexao import obter_conexao
from config import DB_CONFIG, BASE_PATH  # Importado BASE_PATH para gerir o caminho D:\...

def iniciar_bd():
    """
    Cria a base de dados, as tabelas necessárias e garante a existência
    das colunas táticas para alocação de recursos e tipologias de veículos.
    """
    conn_inicial = mysql.connector.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor_inicial = conn_inicial.cursor()
    cursor_inicial.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor_inicial.close()
    conn_inicial.close()

    conn = obter_conexao()
    cursor = conn.cursor()

    # ====================================
    # UTILIZADORES
    # ====================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilizadores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
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
        nome VARCHAR(100) NOT NULL,
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
        vitimas INT DEFAULT 0,
        descricao TEXT,
        latitude DOUBLE,
        longitude DOUBLE,
        estado VARCHAR(50),
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    colunas_novas = [
        ("num_carros", "VARCHAR(255) DEFAULT '0 VTR'"),
        ("num_bombeiros", "INT DEFAULT 0"),
        ("autoridade", "VARCHAR(10) DEFAULT 'NÃO'")
    ]
    
    for nome_coluna, definicao in colunas_novas:
        try:
            cursor.execute(f"ALTER TABLE ocorrencias ADD COLUMN {nome_coluna} {definicao}")
        except mysql.connector.Error as err:
            if err.errno == 1060 or "duplicate" in str(err).lower():
                if nome_coluna == "num_carros":
                    try: cursor.execute("ALTER TABLE ocorrencias MODIFY COLUMN num_carros VARCHAR(255) DEFAULT '0 VTR'")
                    except: pass
            else:
                raise err

    # ====================================
    # DESPACHOS
    # ====================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS despachos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        quartel_id INT,
        ocorrencia_id INT,
        viatura VARCHAR(100),
        bombeiros INT DEFAULT 0,
        estado VARCHAR(50),
        hora_saida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (quartel_id) REFERENCES quarteis(id) ON DELETE CASCADE,
        FOREIGN KEY (ocorrencia_id) REFERENCES ocorrencias(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    
    # Sincroniza cópia local na pasta dados ao iniciar
    sincronizar_dados_para_csv()
    print("✅ Base de dados e persistência em ficheiro CSV sincronizadas.")


# ==================================================
# 📚 REQUISITO UC: PERSISTÊNCIA NO CAMINHO /dados
# ==================================================
def sincronizar_dados_para_csv():
    """
    Exporta os registos para a pasta D:\...\firecommand\dados, cumprindo
    obrigatoriamente o requisito de persistência em ficheiros locais da UC.
    """
    try:
        # Define e cria o caminho da pasta dados dinamicamente usando o BASE_PATH
        pasta_dados = os.path.join(BASE_PATH, "dados")
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados, exist_ok=True)

        caminho_ocorrencias = os.path.join(pasta_dados, "ocorrencias_backup.csv")
        caminho_quarteis = os.path.join(pasta_dados, "quarteis_backup.csv")

        # 1. Exportar Ocorrências
        conn = obter_conexao()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ocorrencias")
        ocorrencias = cursor.fetchall()
        
        with open(caminho_ocorrencias, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "tipo", "severidade", "vitimas", "descricao", "latitude", "longitude", "estado", "num_carros", "num_bombeiros"])
            for o in ocorrencias:
                writer.writerow([o["id"], o["tipo"], o["severidade"], o["vitimas"], o["descricao"], o["latitude"], o["longitude"], o["estado"], o["num_carros"], o["num_bombeiros"]])
        
        # 2. Exportar Quartéis
        cursor.execute("SELECT * FROM quarteis")
        quarteis = cursor.fetchall()
        
        with open(caminho_quarteis, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nome", "tipo", "distrito", "latitude", "longitude"])
            for q in quarteis:
                writer.writerow([q["id"], q["nome"], q["tipo"], q["distrito"], q["latitude"], q["longitude"]])
                
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Aviso na sincronização do CSV local: {e}")


# ==================================================
# FUNÇÕES AUXILIARES: QUARTÉIS
# ==================================================

def obter_quarteis():
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM quarteis ORDER BY nome")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados


def inserir_quartel(nome, tipo, distrito, latitude, longitude):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO quarteis (nome, tipo, distrito, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, tipo, distrito, latitude, longitude))
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


def eliminar_quartel(nome):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quarteis WHERE nome = %s", (nome,))
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


# ==================================================
# FUNÇÕES AUXILIARES: OCORRÊNCIAS
# ==================================================

def obter_ocorrencias():
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ocorrencias ORDER BY data_criacao DESC")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados


def inserir_ocorrencia(tipo, severidade, vitimas, descricao, latitude, longitude, estado="Ativa"):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ocorrencias (tipo, severidade, vitimas, descricao, latitude, longitude, estado, num_carros, num_bombeiros, autoridade)
        VALUES (%s, %s, %s, %s, %s, %s, %s, '0 VTR', 0, 'NÃO')
    """, (tipo, severidade, vitimas, descricao, latitude, longitude, estado))
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


def alocar_recursos_ocorrencia(ocorrencia_id, qtd_novos_carros, sigla_vtr, novos_bombeiros, autoridade, novo_estado="Em Curso"):
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT num_carros, num_bombeiros, autoridade FROM ocorrencias WHERE id = %s", (ocorrencia_id,))
    atual = cursor.fetchone()
    
    carros_atuais_texto = str(atual["num_carros"]).strip() if atual else "0 VTR"
    bombeiros_atuais = int(atual["num_bombeiros"]) if atual else 0
    autoridade_atual = str(atual["autoridade"]).strip().upper() if atual else "NÃO"

    texto_novo_despacho = f"{qtd_novos_carros}x {sigla_vtr}"
    
    if carros_atuais_texto == "0 VTR" or carros_atuais_texto == "" or carros_atuais_texto == "0":
        texto_final_carros = texto_novo_despacho
    else:
        texto_final_carros = f"{carros_atuais_texto} + {texto_novo_despacho}"

    total_bombeiros = bombeiros_atuais + novos_bombeiros
    status_policia = "SIM" if (autoridade == "SIM" or autoridade_atual == "SIM") else "NÃO"

    cursor.close()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ocorrencias 
        SET num_carros = %s, num_bombeiros = %s, autoridade = %s, estado = %s
        WHERE id = %s
    """, (texto_final_carros, total_bombeiros, status_policia, novo_estado, ocorrencia_id))
    
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


def atualizar_estado_ocorrencia(ocorrencia_id, novo_estado):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ocorrencias 
        SET estado = %s 
        WHERE id = %s
    """, (novo_estado, ocorrencia_id))
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


def eliminar_ocorrencia_por_id(ocorrencia_id):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ocorrencias WHERE id = %s", (ocorrencia_id,))
    conn.commit()
    cursor.close()
    conn.close()
    sincronizar_dados_para_csv()


# ==================================================
# ESTATÍSTICAS
# ==================================================

def total_quarteis():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM quarteis")
    res = cursor.fetchone()
    total = res[0] if res else 0
    cursor.close()
    conn.close()
    return total


def total_ocorrencias():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ocorrencias")
    res = cursor.fetchone()
    total = res[0] if res else 0
    cursor.close()
    conn.close()
    return total


def total_ocorrencias_ativas():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ocorrencias WHERE estado = 'Ativa'")
    res = cursor.fetchone()
    total = res[0] if res else 0
    cursor.close()
    conn.close()
    return total


def total_ocorrencias_em_curso():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ocorrencias WHERE estado = 'Em Curso'")
    res = cursor.fetchone()
    total = res[0] if res else 0
    cursor.close()
    conn.close()
    return total


def total_bombeiros_empenhados():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(num_bombeiros) FROM ocorrencias WHERE estado != 'Resolvida'")
    res = cursor.fetchone()
    total = res[0] if res and res[0] is not None else 0
    cursor.close()
    conn.close()
    return total


def obter_resumo_viaturas_ativas():
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT num_carros FROM ocorrencias WHERE estado != 'Resolvida'")
    linhas = cursor.fetchall()
    cursor.close()
    conn.close()

    lista_vtr = []
    for l in linhas:
        txt = str(l["num_carros"]).strip()
        if txt != "0 VTR" and txt != "" and txt != "0":
            lista_vtr.append(txt)
    
    return " + ".join(lista_vtr) if lista_vtr else "Nenhuma VTR empenhada"
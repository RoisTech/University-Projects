from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API da Ficha 3", 
    description="API gerada com base nos exercícios de Programação de Computadores II"
)

# --- Modelos de Dados (Validação de Input) ---

class Orcamento(BaseModel):
    artigo: str
    preco_unitario: float
    quantidade: int

class Avaliacao(BaseModel):
    uc: str
    nota1: float
    nota2: float
    nota3: float

# --- Endpoints (Rotas da API) ---

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo à API Universitária! Acede a /docs para veres a documentação interativa."}

@app.post("/orcamento")
def calcular_orcamento(dados: Orcamento):
    """Baseado no Exercício 2 - Orçamento de Material Escolar"""
    subtotal = dados.preco_unitario * dados.quantidade
    total_iva = subtotal * 1.23  # IVA 23%
    return {
        "artigo": dados.artigo,
        "subtotal": round(subtotal, 2),
        "total_com_iva": round(total_iva, 2)
    }

@app.post("/avaliacao")
def avaliar_uc(dados: Avaliacao):
    """Baseado no Exercício 5 - Avaliação de uma Unidade Curricular"""
    media = (dados.nota1 + dados.nota2 + dados.nota3) / 3
    aprovado = media >= 10
    return {
        "uc": dados.uc,
        "media": round(media, 2),
        "aprovado": aprovado
    }

@app.get("/consumo")
def calcular_consumo(mes: str, consumo_diario: float):
    """Baseado no Exercício 3 - Estimativa de Consumo de Água (Usando Query Params)"""
    consumo_mensal = consumo_diario * 30
    consumo_m3 = consumo_mensal / 1000
    return {
        "mes": mes,
        "consumo_mensal_litros": round(consumo_mensal, 2),
        "consumo_m3": round(consumo_m3, 2)
    }
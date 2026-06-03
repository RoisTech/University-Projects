import tkinter as tk
from tkinter import ttk, messagebox
import time
import urllib.request
import json
from datetime import datetime

COR_BG = "#1e1e24"
COR_CARD = "#2a2a35"
COR_TEXTO = "#ffffff"
COR_ALERTA = "#ff5555"
COR_TEXTO_MUTED = "#aaaaaa"

def obter_dados_meteorologicos():
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.23&longitude=-8.68&current_weather=true"
    try:
        requisicao = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(requisicao, timeout=3) as resposta:
            dados = json.loads(resposta.read().decode())
            temp = dados['current_weather']['temperature']
            return f"{temp} °C"
    except Exception:
        return "18.5 °C (Offline)"

def carregar_ocorrencias_ativas():
    return [
        {"id": 20260401, "local": "Santarém (Cidade)", "tipo": "Incêndio Urbano", "meios": "12 Operacionais / 4 Viaturas"},
        {"id": 20260402, "local": "Almeirim", "tipo": "Acidente Rodoviário", "meios": "8 Operacionais / 2 Viaturas"},
        {"id": 20260403, "local": "Abrantes", "tipo": "Incêndio Rural", "meios": "24 Operacionais / 6 Viaturas / 1 Helicóptero"},
        {"id": 20260404, "local": "Cartaxo", "tipo": "Limpeza de Via", "meios": "3 Operacionais / 1 Viatura"}
    ]

def atualizar_relogio_e_tempo(janela, label_relogio, label_temp, contador_api):
    hora_atual = datetime.now().strftime("%H:%M:%S")
    label_relogio.config(text=hora_atual)
    
    if contador_api[0] >= 300:
        label_temp.config(text=f"Santarém: {obter_dados_meteorologicos()}")
        contador_api[0] = 0
    else:
        contador_api[0] += 1
        
    janela.after(1000, lambda: atualizar_relogio_e_tempo(janela, label_relogio, label_temp, contador_api))

def pesquisar_ocorrencia(tabela, campo_pesquisa, lista_dados):
    termo = campo_pesquisa.get().lower()
    for item in tabela.get_children():
        tabela.delete(item)
    for o in lista_dados:
        if termo in o['local'].lower() or termo in o['tipo'].lower():
            tabela.insert("", tk.END, values=(o['id'], o['local'], o['tipo'], o['meios']))

def limpar_pesquisa(tabela, campo_pesquisa, lista_dados):
    campo_pesquisa.delete(0, tk.END)
    for item in tabela.get_children():
        tabela.delete(item)
    for o in lista_dados:
        tabela.insert("", tk.END, values=(o['id'], o['local'], o['tipo'], o['meios']))

def mostrar_detalhes(tabela):
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Por favor, selecione uma ocorrência ativa na lista.")
        return
    valores = tabela.item(item_selecionado, 'values')
    messagebox.showinfo("Teatro de Operações", f"Ocorrência N.º: {valores[0]}\nLocalidade: {valores[1]}\nTipologia: {valores[2]}\nMeios Alocados: {valores[3]}")

def inicializar_app():
    dados_ocorrencias = carregar_ocorrencias_ativas()
    raiz = tk.Tk()
    raiz.title("Módulo de Comando e Controlo de Ocorrências Activas")
    raiz.geometry("900x550")
    raiz.configure(bg=COR_BG)
    raiz.resizable(False, False)
    
    frame_topo = tk.Frame(raiz, bg=COR_BG)
    frame_topo.pack(fill=tk.X, padx=20, py=10)
    
    lbl_titulo = tk.Label(frame_topo, text="CODIS - Sala de Situação Virtual", font=("Helvetica", 14, "bold"), fg=COR_ALERTA, bg=COR_BG)
    lbl_titulo.pack(side=tk.LEFT)
    
    lbl_relogio = tk.Label(frame_topo, text="00:00:00", font=("Consolas", 14, "bold"), fg=COR_TEXTO, bg=COR_CARD, px=10, py=4)
    lbl_relogio.pack(side=tk.RIGHT, padx=(10, 0))
    
    temp_atual = obter_dados_meteorologicos()
    lbl_temperatura = tk.Label(frame_topo, text=f"Santarém: {temp_atual}", font=("Helvetica", 10, "bold"), fg="#00ff66", bg=COR_BG)
    lbl_temperatura.pack(side=tk.RIGHT, padx=15)
    
    frame_busca = tk.LabelFrame(raiz, text=" Painel de Filtragem de Emergências (Procura Linear) ", font=("Helvetica", 9, "bold"), fg=COR_TEXTO, bg=COR_CARD, bd=1, relief=tk.SOLID)
    frame_busca.pack(fill=tk.X, padx=20, pady=10, ipady=5)
    
    lbl_info = tk.Label(frame_busca, text="Filtrar por Local/Tipo:", fg=COR_TEXTO_MUTED, bg=COR_CARD, font=("Helvetica", 10))
    lbl_info.pack(side=tk.LEFT, padx=10)
    
    txt_busca = tk.Entry(frame_busca, width=30, font=("Helvetica", 10), bg=COR_BG, fg=COR_TEXTO, insertbackground=COR_TEXTO, bd=1, relief=tk.SOLID)
    txt_busca.pack(side=tk.LEFT, padx=5)
    
    btn_buscar = tk.Button(frame_busca, text="Aplicar Filtro", bg="#444455", fg=COR_TEXTO, bd=0, px=12, py=2, cursor="hand2", command=lambda: pesquisar_ocorrencia(tree, txt_busca, dados_ocorrencias))
    btn_buscar.pack(side=tk.LEFT, padx=5)
    
    btn_limpar = tk.Button(frame_busca, text="Limpar", bg=COR_BG, fg=COR_TEXTO_MUTED, bd=0, px=12, py=2, cursor="hand2", command=lambda: limpar_pesquisa(tree, txt_busca, dados_ocorrencias))
    btn_limpar.pack(side=tk.LEFT, padx=5)

    frame_tabela = tk.Frame(raiz, bg=COR_BG)
    frame_tabela.pack(fill=tk.BOTH, expand=True, padx=20, py=5)
    
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview", background=COR_CARD, foreground=COR_TEXTO, fieldbackground=COR_CARD, rowheight=28, borderwidth=0, font=("Helvetica", 10))
    estilo.configure("Treeview.Heading", background="#3a3a45", foreground=COR_TEXTO, font=("Helvetica", 10, "bold"), borderwidth=0)
    estilo.map("Treeview", background=[("selected", COR_ALERTA)], foreground=[("selected", COR_TEXTO)])
    
    colunas = ("id", "local", "tipo", "meios")
    tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="browse")
    
    tree.heading("id", text="N.º EVENTO")
    tree.heading("local", text="LOCALIDADE")
    tree.heading("tipo", text="TIPOLOGIA DA OCORRÊNCIA")
    tree.heading("meios", text="MEIOS NO TEATRO DE OPERAÇÕES")
    
    tree.column("id", width=100, anchor=tk.CENTER)
    tree.column("local", width=180, anchor=tk.W)
    tree.column("tipo", width=180, anchor=tk.W)
    tree.column("meios", width=380, anchor=tk.W)
    
    for ocorrencia in dados_ocorrencias:
        tree.insert("", tk.END, values=(ocorrencia['id'], ocorrencia['local'], ocorrencia['tipo'], ocorrencia['meios']))
        
    tree.pack(fill=tk.BOTH, expand=True)
    
    frame_botoes = tk.Frame(raiz, bg=COR_BG)
    frame_botoes.pack(fill=tk.X, padx=20, py=15)
    
    btn_detalhe = tk.Button(frame_botoes, text="🚨 Inspecionar Teatro de Operações", font=("Helvetica", 10, "bold"), bg=COR_ALERTA, fg=COR_TEXTO, bd=0, py=6, px=15, cursor="hand2", command=lambda: mostrar_detalhes(tree))
    btn_detalhe.pack(side=tk.LEFT)
    
    lbl_status = tk.Label(frame_botoes, text="● Sistema Operacional em Tempo Real", fg="#00ff66", bg=COR_BG, font=("Helvetica", 9, "italic"))
    lbl_status.pack(side=tk.RIGHT, py=6)

    contador_atualizacao_api = [0]
    atualizar_relogio_e_tempo(raiz, lbl_relogio, lbl_temperatura, contador_atualizacao_api)
    
    raiz.mainloop()

if __name__ == "__main__":
    inicializar_app()

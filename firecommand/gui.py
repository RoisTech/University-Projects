import tkinter as tk
from tkinter import messagebox

from utils.ficheiros import ler_csv
from core.simulador import simular
from modulos.analise import estatisticas
from modulos.incidentes import guardar_incidente
from modulos.recursos import guardar_recurso
from modulos.ia import gerar_cenario
import os

# =========================
# INICIALIZAR DADOS (NOVO)
# =========================

base = "dados"

incidentes_path = os.path.join(base, "incidentes.csv")
recursos_path = os.path.join(base, "recursos.csv")

os.makedirs(base, exist_ok=True)

# criar cabeçalho incidentes
if not os.path.exists(incidentes_path):
    with open(incidentes_path, "w", encoding="utf-8") as f:
        f.write("tipo,gravidade,vento,temperatura,x,y\n")

# criar cabeçalho recursos
if not os.path.exists(recursos_path):
    with open(recursos_path, "w", encoding="utf-8") as f:
        f.write("bombeiros,veiculos\n")

# =========================
# FUNÇÕES
# =========================

def novo_incidente():
    janela = tk.Toplevel()
    janela.title("Novo Incidente")

    entries = {}

    for campo in ["tipo", "gravidade", "vento", "temperatura", "x", "y"]:
        tk.Label(janela, text=campo).pack()
        e = tk.Entry(janela)
        e.pack()
        entries[campo] = e

    def guardar():
        try:
            incidente = {k: int(v.get()) if k != "tipo" else v.get() for k, v in entries.items()}
            guardar_incidente(incidente)
            messagebox.showinfo("OK", "Guardado!")
            janela.destroy()
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    tk.Button(janela, text="Guardar", command=guardar).pack()


def novo_recurso():
    janela = tk.Toplevel()
    janela.title("Recursos")

    b = tk.Entry(janela)
    v = tk.Entry(janela)

    tk.Label(janela, text="Bombeiros").pack()
    b.pack()
    tk.Label(janela, text="Veículos").pack()
    v.pack()

    def guardar():
        try:
            guardar_recurso({
                "bombeiros": int(b.get()),
                "veiculos": int(v.get())
            })
            messagebox.showinfo("OK", "Guardado!")
            janela.destroy()
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    tk.Button(janela, text="Guardar", command=guardar).pack()


def executar_sim():
    messagebox.showinfo("Simulação", simular())


def ver_stats():
    messagebox.showinfo("Stats", estatisticas())


def gerar_ia_gui():
    c = gerar_cenario()
    guardar_incidente(c)
    messagebox.showinfo("IA", f"Cenário criado!\nLocal: ({c['x']},{c['y']})")


def mapa():
    dados = ler_csv("dados/incidentes.csv")

    if not dados:
        messagebox.showerror("Erro", "Sem incidentes!")
        return

    inc_valido = None

    for inc in reversed(dados):
        try:
            x = int(inc["x"])
            y = int(inc["y"])
            inc_valido = inc
            break
        except:
            continue

    if not inc_valido:
        messagebox.showerror("Erro", "Nenhum dado válido!")
        return

    x = int(inc_valido["x"])
    y = int(inc_valido["y"])

    win = tk.Toplevel()
    win.title("Mapa")

    canvas = tk.Canvas(win, width=300, height=300)
    canvas.pack()

    size = 30

    for i in range(10):
        for j in range(10):
            canvas.create_rectangle(i*size, j*size, (i+1)*size, (j+1)*size)

    canvas.create_rectangle(x*size, y*size, (x+1)*size, (y+1)*size, fill="red")


# =========================
# UI
# =========================

root = tk.Tk()
root.title("FireCommand")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

tk.Label(root, text="🔥 FireCommand", fg="white", bg="#1e1e1e", font=("Arial", 20)).pack(pady=20)

def btn(txt, cmd):
    return tk.Button(root, text=txt, width=30, height=2, command=cmd)

btn("Novo Incidente", novo_incidente).pack(pady=5)
btn("Adicionar Recursos", novo_recurso).pack(pady=5)
btn("Simular", executar_sim).pack(pady=5)
btn("Estatísticas", ver_stats).pack(pady=5)
btn("Gerar Cenário IA", gerar_ia_gui).pack(pady=5)
btn("Ver Mapa", mapa).pack(pady=5)

root.mainloop()
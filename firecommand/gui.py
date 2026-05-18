import os
from tkinter import messagebox

import mysql.connector
import ttkbootstrap as ttk
from tkintermapview import TkinterMapView
from ttkbootstrap.constants import *

from config import (
    DB_CONFIG,
    FORMACAO_PATH,
    THEME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)


class FireCommandGUI:

    def __init__(self):

        self.app = ttk.Window(
            title="🚒 FireCommand Pro - Centro Operacional",
            themename=THEME,
            size=(WINDOW_WIDTH, WINDOW_HEIGHT),
            resizable=(True, True)
        )

        self.modo_mapa = None
        self.quartel_temp = {}
        self.ocorrencia_temp = {}

        self.criar_interface()
        self.carregar_quarteis()
        self.carregar_ocorrencias()

    # ==================================================
    # BASE DE DADOS
    # ==================================================

    def ligar_bd(self):

        return mysql.connector.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        # ==========================================
        # SIDEBAR
        # ==========================================

        self.sidebar = ttk.Frame(
            self.app,
            width=350
        )

        self.sidebar.pack(
            side=LEFT,
            fill=Y
        )

        ttk.Label(
            self.sidebar,
            text="🚒 FIRECOMMAND",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=20)

        ttk.Separator(self.sidebar).pack(
            fill=X,
            padx=10,
            pady=10
        )

        # ==========================================
        # BOTÕES
        # ==========================================

        botoes = [

            ("🚒 Quartéis", "danger", self.abrir_quarteis),
            ("🔥 Ocorrências", "warning", self.abrir_ocorrencias),
            ("🚒 Despacho", "info", self.abrir_despacho),
            ("📚 Formação", "secondary", self.abrir_formacao),
            ("📊 Estatísticas", "success", self.abrir_estatisticas),
            ("❌ Sair", "secondary", self.app.destroy)

        ]

        for texto, estilo, comando in botoes:

            ttk.Button(
                self.sidebar,
                text=texto,
                bootstyle=estilo,
                command=comando
            ).pack(
                fill=X,
                padx=10,
                pady=5
            )

        # ==========================================
        # LISTA QUARTÉIS
        # ==========================================

        ttk.Label(
            self.sidebar,
            text="🚒 Quartéis",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

        self.lista_quarteis = ttk.Treeview(
            self.sidebar,
            columns=("nome",),
            show="headings",
            height=8
        )

        self.lista_quarteis.heading(
            "nome",
            text="Nome"
        )

        self.lista_quarteis.pack(
            fill=X,
            padx=10,
            pady=5
        )

        # ==========================================
        # MAPA
        # ==========================================

        self.frame_mapa = ttk.Frame(self.app)

        self.frame_mapa.pack(
            fill=BOTH,
            expand=True
        )

        self.mapa = TkinterMapView(
            self.frame_mapa,
            corner_radius=0
        )

        self.mapa.pack(
            fill=BOTH,
            expand=True
        )

        # MAPA CLARO PROFISSIONAL

        self.mapa.set_tile_server(
            "https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
        )

        self.mapa.set_position(
            39.5,
            -8.0
        )

        self.mapa.set_zoom(7)

        self.mapa.add_left_click_map_command(
            self.clique_mapa
        )

    # ==================================================
    # QUARTÉIS
    # ==================================================

    def abrir_quarteis(self):

        janela = ttk.Toplevel(self.app)

        janela.title("🚒 Criar Quartel")
        janela.geometry("450x420")

        ttk.Label(janela, text="Nome Quartel").pack(pady=5)

        nome_entry = ttk.Entry(janela, width=40)
        nome_entry.pack()

        ttk.Label(janela, text="Tipo").pack(pady=5)

        tipo_combo = ttk.Combobox(
            janela,
            values=[
                "Voluntários",
                "Sapadores",
                "Municipais"
            ],
            state="readonly"
        )

        tipo_combo.pack()
        tipo_combo.set("Voluntários")

        ttk.Label(janela, text="Distrito").pack(pady=5)

        distrito_combo = ttk.Combobox(
            janela,
            values=[
                "Aveiro", "Beja", "Braga", "Bragança",
                "Castelo Branco", "Coimbra", "Évora",
                "Faro", "Guarda", "Leiria", "Lisboa",
                "Portalegre", "Porto", "Santarém",
                "Setúbal", "Viana do Castelo",
                "Vila Real", "Viseu"
            ],
            state="readonly"
        )

        distrito_combo.pack()
        distrito_combo.set("Lisboa")

        def selecionar_local():

            nome = nome_entry.get().strip()

            if not nome:
                messagebox.showerror(
                    "Erro",
                    "Introduza o nome do quartel."
                )
                return

            self.quartel_temp = {
                "nome": nome,
                "tipo": tipo_combo.get(),
                "distrito": distrito_combo.get()
            }

            self.modo_mapa = "quartel"

            messagebox.showinfo(
                "Mapa",
                "Clique no mapa para posicionar o quartel."
            )

            janela.destroy()

        ttk.Button(
            janela,
            text="📍 Escolher Localização",
            bootstyle="danger",
            command=selecionar_local
        ).pack(pady=20)

    # ==================================================
    # OCORRÊNCIAS
    # ==================================================

    def abrir_ocorrencias(self):

        messagebox.showinfo(
            "Ocorrências",
            "Clique no mapa para criar ocorrências (próxima fase)."
        )

    # ==================================================
    # DESPACHO
    # ==================================================

    def abrir_despacho(self):

        messagebox.showinfo(
            "Despacho",
            "🚒 Sistema de despacho em desenvolvimento."
        )

    # ==================================================
    # ESTATÍSTICAS
    # ==================================================

    def abrir_estatisticas(self):

        conexao = self.ligar_bd()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM quarteis"
        )

        total_quarteis = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM ocorrencias"
        )

        total_ocorrencias = cursor.fetchone()[0]

        cursor.close()
        conexao.close()

       
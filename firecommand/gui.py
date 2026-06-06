import os
from tkinter import messagebox
import ttkbootstrap as ttk
from tkintermapview import TkinterMapView

# Importação da biblioteca de Geocodificação Automática
from geopy.geocoders import Nominatim

# Importação do manipulador de imagens nativo do Tkinter/Pillow
from PIL import Image, ImageTk

# Importação explícita das constantes
from ttkbootstrap.constants import LEFT, RIGHT, Y, X, BOTH, W, BOTTOM

# Importações de configuração
from config import (
    FORMACAO_PATH,
    THEME,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    DISTRITOS,
    BASE_PATH
)

# Importações das funções centralizadas da Base de Dados
from database.db import (
    obter_quarteis,
    inserir_quartel,
    eliminar_quartel,
    obter_ocorrencias,
    inserir_ocorrencia,
    alocar_recursos_ocorrencia,
    eliminar_ocorrencia_por_id,
    atualizar_estado_ocorrencia,
    total_quarteis,
    total_ocorrencias,
    total_ocorrencias_ativas,
    total_ocorrencias_em_curso,
    total_bombeiros_empenhados,
    obter_resumo_viaturas_ativas  # Nova função importada
)


class FireCommandGUI:

    def __init__(self):
        self.app = ttk.Window(
            title="🚒 FireCommand Pro - Centro Operacional",
            themename=THEME,
            size=(WINDOW_WIDTH, WINDOW_HEIGHT),
            resizable=(True, True)
        )

        self.geolocator = Nominatim(user_agent="firecommand_pro_application")

        self.modo_mapa = None
        self.quartel_temp = {}
        self.ocorrencia_temp = {}

        # Carregar repositório de ícones gráficos PNG transparentes
        self.pasta_imagens = os.path.join(BASE_PATH, "formacao", "imagens")
        self.carregar_icones_sistema()

        # Inicialização da interface e carregamento de dados
        self.criar_interface()
        self.atualizar_mapa_global()

    def carregar_icones_sistema(self):
        try:
            p_quartel = os.path.join(self.pasta_imagens, "quartel.png")
            p_fogo = os.path.join(self.pasta_imagens, "fogo.png")

            self.icon_quartel = ImageTk.PhotoImage(Image.open(p_quartel).resize((35, 35))) if os.path.exists(p_quartel) else None
            self.icon_fogo = ImageTk.PhotoImage(Image.open(p_fogo).resize((35, 35))) if os.path.exists(p_fogo) else None
            self.icon_invisivel = ImageTk.PhotoImage(Image.new("RGBA", (1, 1), (0, 0, 0, 0)))
        except Exception as e:
            print(f"Aviso ao carregar ícones gráficos: {e}")
            self.icon_quartel = None
            self.icon_fogo = None
            self.icon_invisivel = None

    # ==================================================
    # INTERFACE PRINCIPAL
    # ==================================================

    def criar_interface(self):
        self.sidebar = ttk.Frame(self.app, width=350)
        self.sidebar.pack(side=LEFT, fill=Y)

        ttk.Label(self.sidebar, text="🚒 FIRECOMMAND", font=("Segoe UI", 24, "bold")).pack(pady=20)
        ttk.Separator(self.sidebar).pack(fill=X, padx=10, pady=10)

        botoes = [
            ("🚒 Quartéis", "danger", self.abrir_quarteis),
            ("🔥 Ocorrências", "warning", self.abrir_ocorrencias),
            ("🚒 Despacho", "info", self.abrir_despacho),
            ("📚 Formação", "secondary", self.abrir_formacao),
            ("📊 Estatísticas", "success", self.abrir_estatisticas),
            ("❌ Sair", "secondary", self.app.destroy)
        ]

        for texto, estilo, comando in botoes:
            ttk.Button(self.sidebar, text=texto, bootstyle=estilo, command=comando).pack(fill=X, padx=10, pady=5)

        ttk.Label(self.sidebar, text="🚒 Quartéis Registados", font=("Segoe UI", 12, "bold")).pack(pady=10)

        self.lista_quarteis = ttk.Treeview(self.sidebar, columns=("nome",), show="headings", height=10)
        self.lista_quarteis.heading("nome", text="Nome")
        self.lista_quarteis.column("nome", width=250)
        self.lista_quarteis.pack(fill=X, padx=10, pady=5)

        ttk.Button(self.sidebar, text="❌ Remover Quartel", bootstyle="secondary-outline", command=self.remover_quartel_selecionado).pack(fill=X, padx=10, pady=5)

        self.frame_mapa = ttk.Frame(self.app)
        self.frame_mapa.pack(fill=BOTH, expand=True)

        self.mapa = TkinterMapView(self.frame_mapa, corner_radius=0)
        self.mapa.pack(fill=BOTH, expand=True)
        self.mapa.set_tile_server("https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png")
        self.mapa.set_position(39.5, -8.0)
        self.mapa.set_zoom(7)
        self.mapa.add_left_click_map_command(self.clique_mapa)

    def atualizar_mapa_global(self):
        try:
            self.mapa.delete_all_marker()
        except:
            pass
        self.carregar_quarteis()
        self.carregar_ocorrencias()

    def remover_quartel_selecionado(self):
        selecao = self.lista_quarteis.selection()
        if not selecao:
            messagebox.showwarning("Seleção", "Por favor, selecione um quartel da lista para remover.")
            return
        item_id = selecao[0]
        nome_quartel = self.lista_quarteis.item(item_id, "values")[0]
        if messagebox.askyesno("Confirmar", f"Deseja eliminar o '{nome_quartel}'?"):
            try:
                eliminar_quartel(nome_quartel)
                self.atualizar_mapa_global()
                messagebox.showinfo("Sucesso", "Quartel removido.")
            except Exception as erro:
                messagebox.showerror("Erro", str(erro))

    def clique_mapa(self, coordenadas):
        latitude = float(coordenadas[0])
        longitude = float(coordenadas[1])

        if self.modo_mapa == "quartel":
            try:
                inserir_quartel(nome=self.quartel_temp["nome"], tipo=self.quartel_temp["tipo"], distrito=self.quartel_temp["distrito"], latitude=latitude, longitude=longitude)
                self.atualizar_mapa_global()
                self.quartel_temp = {}
                self.modo_mapa = None
                messagebox.showinfo("Sucesso", "Quartel guardado.")
            except Exception as erro:
                messagebox.showerror("Erro", str(erro))

        elif self.modo_mapa == "ocorrencia":
            try:
                inserir_ocorrencia(tipo=self.ocorrencia_temp["tipo"], severidade=self.ocorrencia_temp["severidade"], vitimas=self.ocorrencia_temp["vitimas"], descricao=self.ocorrencia_temp["descricao"], latitude=latitude, longitude=longitude, estado="Ativa")
                self.atualizar_mapa_global()
                self.ocorrencia_temp = {}
                self.modo_mapa = None
                messagebox.showinfo("Sucesso", "Ocorrência ativa registada.")
            except Exception as erro:
                messagebox.showerror("Erro", str(erro))

    def abrir_quarteis(self):
        janela = ttk.Toplevel(master=self.app)
        janela.title("🚒 Criar Quartel")
        janela.geometry("450x520")

        ttk.Label(janela, text="Nome Quartel").pack(pady=5)
        nome_entry = ttk.Entry(janela, width=40)
        nome_entry.pack()

        ttk.Label(janela, text="Tipo").pack(pady=5)
        tipo_combo = ttk.Combobox(janela, values=["Voluntários", "Sapadores", "Municipais"], state="readonly")
        tipo_combo.pack()
        tipo_combo.set("Voluntários")

        ttk.Label(janela, text="Distrito").pack(pady=5)
        distrito_combo = ttk.Combobox(janela, values=DISTRITOS, state="readonly")
        distrito_combo.pack()
        distrito_combo.set("Lisboa")

        ttk.Label(janela, text="Morada / Localidade").pack(pady=5)
        morada_entry = ttk.Entry(janela, width=40)
        morada_entry.pack()

        def submeter_quartel():
            nome = nome_entry.get().strip()
            morada = morada_entry.get().strip()
            if not nome:
                messagebox.showerror("Erro", "Nome obrigatório.")
                return

            if morada:
                try:
                    localizacao = self.geolocator.geocode(f"{morada}, Portugal")
                    if localizacao:
                        inserir_quartel(nome=nome, tipo=tipo_combo.get(), distrito=distrito_combo.get(), latitude=localizacao.latitude, longitude=localizacao.longitude)
                        self.atualizar_mapa_global()
                        self.mapa.set_position(localizacao.latitude, localizacao.longitude)
                        janela.destroy()
                        return
                except: pass

            self.quartel_temp = {"nome": nome, "tipo": tipo_combo.get(), "distrito": distrito_combo.get()}
            self.modo_mapa = "quartel"
            messagebox.showinfo("Manual", "Clique no mapa.")
            janela.destroy()

        ttk.Button(janela, text="💾 Confirmar", bootstyle="danger", command=submeter_quartel).pack(pady=20)

    def carregar_quarteis(self):
        try:
            for item in self.lista_quarteis.get_children():
                self.lista_quarteis.delete(item)
            dados = obter_quarteis()
            for q in dados:
                self.lista_quarteis.insert("", "end", values=(q["nome"],))
                if q["latitude"] is not None and q["longitude"] is not None:
                    self.mapa.set_marker(float(q["latitude"]), float(q["longitude"]), text=f"🚒 {q['nome']}", icon=self.icon_quartel)
        except Exception as erro:
            print(erro)

    def abrir_ocorrencias(self):
        janela = ttk.Toplevel(master=self.app)
        janela.title("🔥 Nova Ocorrência")
        janela.geometry("450x560")

        ttk.Label(janela, text="Tipo de Incidente").pack(pady=5)
        tipo_combo = ttk.Combobox(janela, values=["Incêndio Florestal", "Incêndio Urbano", "Acidente Rodoviário", "Inundação", "Resgate"], state="readonly")
        tipo_combo.pack()
        tipo_combo.set("Incêndio Florestal")

        ttk.Label(janela, text="Severidade").pack(pady=5)
        severidade_combo = ttk.Combobox(janela, values=["Ligeira", "Moderada", "Grave", "Crítica"], state="readonly")
        severidade_combo.pack()
        severidade_combo.set("Moderada")

        ttk.Label(janela, text="Vítimas").pack(pady=5)
        vitimas_entry = ttk.Entry(janela, width=15)
        vitimas_entry.pack()
        vitimas_entry.insert(0, "0")

        ttk.Label(janela, text="Descrição").pack(pady=5)
        desc_entry = ttk.Entry(janela, width=40)
        desc_entry.pack()

        ttk.Label(janela, text="Morada / Localidade").pack(pady=5)
        local_entry = ttk.Entry(janela, width=40)
        local_entry.pack()

        def submeter_ocorrencia():
            try: vits = int(vitimas_entry.get().strip())
            except: return
            morada = local_entry.get().strip()

            if morada:
                try:
                    localizacao = self.geolocator.geocode(f"{morada}, Portugal")
                    if localizacao:
                        inserir_ocorrencia(tipo=tipo_combo.get(), severidade=severidade_combo.get(), vitimas=vits, descricao=desc_entry.get().strip(), latitude=localizacao.latitude, longitude=localizacao.longitude, estado="Ativa")
                        self.atualizar_mapa_global()
                        self.mapa.set_position(localizacao.latitude, localizacao.longitude)
                        janela.destroy()
                        return
                except: pass

            self.ocorrencia_temp = {"tipo": tipo_combo.get(), "severidade": severidade_combo.get(), "vitimas": vits, "descricao": desc_entry.get().strip()}
            self.modo_mapa = "ocorrencia"
            messagebox.showinfo("Manual", "Clique no mapa.")
            janela.destroy()

        ttk.Button(janela, text="📍 Confirmar", bootstyle="warning", command=submeter_ocorrencia).pack(pady=20)

    # ==================================================
    # 🎨 REPOSICIONAMENTO MÁXIMO E ALINHAMENTO COLADO
    # ==================================================

    def carregar_ocorrencias(self):
        try:
            ocorrencias = obter_ocorrencias()
            for o in ocorrencias:
                if o.get("latitude") is not None and o.get("longitude") is not None:
                    if o.get("estado") == "Resolvida":
                        continue

                    lat = float(o["latitude"])
                    lon = float(o["longitude"])

                    texto_marcador = f"{o['tipo']} ({o['severidade']})"
                    self.mapa.set_marker(lat, lon, text=texto_marcador, icon=self.icon_fogo)

                    vtr_texto = str(o.get("num_carros", "0 VTR")).strip()
                    bombeiros = int(o.get("num_bombeiros", 0))
                    policia_presente = str(o.get("autoridade", "NÃO")).strip().upper()

                    # Calibração milimétrica colada (Reduzido offset de 0.0035 para 0.0006)
                    if vtr_texto != "0 VTR" and vtr_texto != "" and vtr_texto != "0":
                        self.mapa.set_marker(lat, lon - 0.0006, text=f"导 [{vtr_texto}]", icon=self.icon_invisivel, text_color="red")
                        
                    if bombeiros > 0:
                        texto_humanos = f"🧑‍🚒 [{bombeiros} BO]"
                        if policia_presente == "SIM":
                            texto_humanos += " 聚 [POLÍCIA]"
                        self.mapa.set_marker(lat, lon + 0.0006, text=texto_humanos, icon=self.icon_invisivel, text_color="orange")
        except Exception as erro:
            print(erro)

    # ==================================================
    # MÓDULO: DESPACHO
    # ==================================================

    def abrir_despacho(self):
        janela = ttk.Toplevel(master=self.app)
        janela.title("🚒 Painel Operacional de Despacho de Meios")
        janela.geometry("750x640")
        janela.resizable(False, False)

        frame_superior = ttk.Frame(janela, padding=10)
        frame_superior.pack(fill=X, expand=False)

        ttk.Label(frame_superior, text="🚨 Selecione a Ocorrência para Operação", font=("Segoe UI", 12, "bold")).pack(pady=5)

        tv = ttk.Treeview(frame_superior, columns=("id", "tipo", "severidade", "estado"), show="headings", height=5)
        tv.heading("id", text="ID")
        tv.heading("tipo", text="Incidente")
        tv.heading("severidade", text="Gravidade")
        tv.heading("estado", text="Estado")
        tv.column("id", width=50, anchor="center")
        tv.column("tipo", width=240)
        tv.column("severidade", width=120, anchor="center")
        tv.column("estado", width=120, anchor="center")
        tv.pack(fill=X)

        def atualizar_tabela_despacho():
            for item in tv.get_children(): 
                tv.delete(item)
            try:
                lista = obter_ocorrencias()
                for o in lista: 
                    tv.insert("", "end", values=(o["id"], o["tipo"], o["severidade"], o["estado"]))
            except Exception as e: 
                print(e)

        atualizar_tabela_despacho()

        frame_inferior = ttk.Frame(janela, padding=10)
        frame_inferior.pack(fill=X, side=BOTTOM, pady=5)

        frame_parametros = ttk.LabelFrame(frame_inferior, text=" Parametrização de Recursos a Despachar ")
        frame_parametros.pack(fill=X, padx=15, pady=15)

        ttk.Label(frame_parametros, text="Tipo de Viatura:").grid(row=0, column=0, sticky=W, pady=5, padx=10)
        tipo_vtr_combo = ttk.Combobox(frame_parametros, values=["ABSC (Ambulância)", "VFCI (Combate)", "VTTU (Tanque)", "VCOT (Comando)", "VETA (Apoio)", "VLCI (Ligeiro)"], state="readonly", width=18)
        tipo_vtr_combo.grid(row=0, column=1, sticky=W, padx=10, pady=5)
        tipo_vtr_combo.set("VFCI (Combate)")

        ttk.Label(frame_parametros, text="Quantidade de Viaturas:").grid(row=1, column=0, sticky=W, pady=5, padx=10)
        carros_entry = ttk.Entry(frame_parametros, width=10)
        carros_entry.grid(row=1, column=1, sticky=W, padx=10, pady=5)
        carros_entry.insert(0, "1")

        ttk.Label(frame_parametros, text="Efetivo Operacional (Bombeiros):").grid(row=2, column=0, sticky=W, pady=5, padx=10)
        bombeiros_entry = ttk.Entry(frame_parametros, width=10)
        bombeiros_entry.grid(row=2, column=1, sticky=W, padx=10, pady=5)
        bombeiros_entry.insert(0, "5")

        autoridade_var = ttk.BooleanVar(value=False)
        chk_autoridade = ttk.Checkbutton(frame_parametros, text="Autoridade Policial (GNR / PSP) presente no local", variable=autoridade_var, bootstyle="round-toggle")
        chk_autoridade.grid(row=3, column=0, columnspan=2, sticky=W, pady=10, padx=10)

        def alterar_estado_selecionado():
            selecao = tv.selection()
            if not selecao: return
            id_ocorrencia = tv.item(selecao[0], "values")[0]

            janela_estado = ttk.Toplevel(master=janela)
            janela_estado.title("Mudar Estado")
            janela_estado.geometry("300x180")
            janela_estado.resizable(False, False)

            ttk.Label(janela_estado, text=f"Novo estado para #{id_ocorrencia}:", font=("Segoe UI", 10, "bold")).pack(pady=10)
            estado_combo = ttk.Combobox(janela_estado, values=["Ativa", "Em Curso", "Resolvida"], state="readonly")
            estado_combo.pack(pady=5)
            estado_combo.set("Em Curso")

            def salvar_novo_estado():
                atualizar_estado_ocorrencia(id_ocorrencia, estado_combo.get())
                self.atualizar_mapa_global()
                atualizar_tabela_despacho()
                janela_estado.destroy()

            ttk.Button(janela_estado, text="Gravar Estado", bootstyle="success", command=salvar_novo_estado).pack(pady=15)

        def fechar_e_eliminar_ocorrencia():
            selecao = tv.selection()
            if not selecao: return
            id_real = tv.item(selecao[0], "values")[0]
            if messagebox.askyesno("Confirmar", f"Deseja APAGAR a ocorrência #{id_real}?"):
                try:
                    eliminar_ocorrencia_por_id(id_real)
                    self.atualizar_mapa_global()
                    atualizar_tabela_despacho()
                except Exception as ex: messagebox.showerror("Erro", str(ex))

        def confirmar_ordem_despacho():
            selecao = tv.selection()
            if not selecao: 
                messagebox.showwarning("Aviso", "Por favor, selecione uma ocorrência ativa na tabela.")
                return
                
            id_ocorrencia = tv.item(selecao[0], "values")[0]
            sigla_viatura = tipo_vtr_combo.get().split(" ")[0]
            
            try:
                alocar_recursos_ocorrencia(
                    ocorrencia_id=id_ocorrencia,
                    qtd_novos_carros=int(carros_entry.get().strip()),
                    sigla_vtr=sigla_viatura,
                    novos_bombeiros=int(bombeiros_entry.get().strip()),
                    autoridade="SIM" if autoridade_var.get() else "NÃO"
                )
                self.atualizar_mapa_global()
                messagebox.showinfo("Sucesso", f"Reforços despachados com sucesso!")
                janela.destroy()
            except Exception as erro: 
                messagebox.showerror("Erro no Despacho", str(erro))

        frame_botoes_acao = ttk.Frame(frame_inferior)
        frame_botoes_acao.pack(fill=X, pady=5)

        ttk.Button(frame_botoes_acao, text="🚀 Ordem de Despacho", bootstyle="info", command=confirmar_ordem_despacho).pack(side=LEFT, padx=5)
        ttk.Button(frame_botoes_acao, text="🔄 Mudar Estado", bootstyle="warning-outline", command=alterar_estado_selecionado).pack(side=LEFT, padx=5)
        ttk.Button(frame_botoes_acao, text="❌ Eliminar Registo", bootstyle="danger-outline", command=fechar_e_eliminar_ocorrencia).pack(side=RIGHT, padx=5)

    def abrir_formacao(self):
        try:
            if os.path.exists(FORMACAO_PATH): os.startfile(FORMACAO_PATH)
            else: os.makedirs(FORMACAO_PATH, exist_ok=True); os.startfile(FORMACAO_PATH)
        except Exception as erro: print(erro)

    # ==================================================
    # 📊 REPORT EXPANDIDO E ATUALIZADO
    # ==================================================

    def abrir_estatisticas(self):
        try:
            tot_q = total_quarteis()
            tot_o_historico = total_ocorrencias()
            tot_ativas = total_ocorrencias_ativas()
            tot_curso = total_ocorrencias_em_curso()
            bo_total = total_bombeiros_empenhados()
            
            # Nova chamada dinâmica que recolhe o texto acumulado de todas as VTRs
            viaturas_detalhadas = obter_resumo_viaturas_ativas()

            relatorio = (
                "📊 **RELATÓRIO OPERACIONAL DO CENTRO DE COMANDO** 📊\n"
                "--------------------------------------------------\n\n"
                f"🚒 **Infraestruturas:**\n"
                f"• Quartéis Operativos Registados: {tot_q}\n\n"
                f"🚨 **Estado Atual do Teatro de Operações:**\n"
                f"• Emergências em Espera (Ativas): {tot_ativas}\n"
                f"• Emergências com Meios no Local (Em Curso): {tot_curso}\n"
                f"• Histórico Total de Ocorrências: {tot_o_historico}\n\n"
                f"🧑‍🚒 **Recursos Humanos Mobilizados:**\n"
                f"• Efetivo Operacional (Bombeiros): {bo_total} Elementos\n\n"
                f"📦 **Meios Materiais Mobilizados:**\n"
                f"• Listagem das Viaturas no Terreno:\n  [ {viaturas_detalhadas} ]"
            )

            messagebox.showinfo("📊 Estatísticas em Tempo Real", relatorio)
        except Exception as erro: 
            messagebox.showerror("Erro nas Estatísticas", f"Não foi possível processar o relatório:\n{erro}")

    def iniciar(self):
        self.app.mainloop()


if __name__ == "__main__":
    sistema = FireCommandGUI()
    sistema.iniciar()
# core/mapa.py
import os
from PIL import Image, ImageTk
import ttkbootstrap as tb

# caminho relativo ao diretório onde corres main.py
MAP_PATH = os.path.join("assets", "imagens", "mapa_portugal.png")
# garante que o nome do ficheiro é igual ao que tens (pode ser .jpg)


def criar_widget_mapa(parent):
    """
    parent: frame onde o mapa vai ficar (por exemplo, um Frame no lado direito).
    devolve: (frame_mapa, label_mapa)
    """

    frame_mapa = tb.Frame(parent)
    frame_mapa.pack(side="right", fill="both", expand=True)

    # confirmar caminho absoluto (só para debug se precisares)
    # print(os.path.abspath(MAP_PATH))

    img = Image.open(MAP_PATH)

    # redimensionar para caber melhor
    largura_base = 800
    ratio = largura_base / img.width
    nova_altura = int(img.height * ratio)
    img = img.resize((largura_base, nova_altura), Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)

    label_mapa = tb.Label(frame_mapa, image=photo)
    label_mapa.image = photo  # manter referência
    label_mapa.pack(fill="both", expand=True)

    return frame_mapa, label_mapa

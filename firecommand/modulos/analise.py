from utils.ficheiros import ler_csv

def estatisticas():
    incidentes = ler_csv("dados/incidentes.csv")

    if not incidentes:
        return "Sem dados"

    total = len(incidentes)
    media = sum(int(i["gravidade"]) for i in incidentes if "gravidade" in i) / total

    return f"Total: {total}\nMédia Gravidade: {round(media,2)}"
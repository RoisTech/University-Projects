from utils.ficheiros import ler_csv

def simular():
    incidentes = ler_csv("dados/incidentes.csv")
    recursos = ler_csv("dados/recursos.csv")

    if not incidentes or not recursos:
        return "⚠️ Dados insuficientes"

    # procurar incidente válido
    inc_valido = None
    for inc in reversed(incidentes):
        if all(k in inc for k in ["vento", "temperatura"]):
            try:
                int(inc["vento"])
                int(inc["temperatura"])
                inc_valido = inc
                break
            except:
                continue

    if not inc_valido:
        return "⚠️ Nenhum incidente válido"

    rec = recursos[-1]

    vento = int(inc_valido["vento"])
    temp = int(inc_valido["temperatura"])

    terreno_factor = 1.5 if inc_valido.get("terreno") == "floresta" else 1

    propagacao = (vento * 0.6 + temp * 0.4) * terreno_factor
    capacidade = int(rec["bombeiros"]) * 2 + int(rec["veiculos"]) * 3

    resultado = capacidade - propagacao

    texto = f"Propagação: {round(propagacao,2)}\nCapacidade: {capacidade}\n"

    if resultado < 0:
        texto += "❌ Incêndio fora de controlo!"
    else:
        texto += "✅ Incêndio controlado!"

    return texto
import random

def gerar_cenario():
    return {
        "tipo": random.choice(["Florestal", "Urbano"]),
        "gravidade": random.randint(3, 10),
        "vento": random.randint(5, 30),
        "temperatura": random.randint(15, 40),
        "x": random.randint(0, 9),
        "y": random.randint(0, 9)
    }
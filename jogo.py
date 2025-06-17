# jogo.py

# --- Definindo as cartas ---
carta1 = {"nome": "Leão", "forca": 8, "velocidade": 7}
carta2 = {"nome": "Elefante", "forca": 9, "velocidade": 4}

# --- Comparando as cartas ---
atributo = input("Escolha o atributo para comparar (forca ou velocidade): ")

if carta1[atributo] > carta2[atributo]:
    print(f"{carta1['nome']} vence com {atributo} maior!")
elif carta2[atributo] > carta1[atributo]:
    print(f"{carta2['nome']} vence com {atributo} maior!")
else:
    print("Empate!")

# --- Verificando quem vence ---
def comparar(cartas, atributo):
    c1, c2 = cartas
    if c1[atributo] > c2[atributo]:
        return f"{c1['nome']} vence!"
    elif c2[atributo] > c1[atributo]:
        return f"{c2['nome']} vence!"
    else:
        return "Empate!"
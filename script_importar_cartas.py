from modelos import *
import json
from sqlalchemy.orm import Session

# ler listacartas e converter para lista
with open("listacartas.json") as file:
    cartas_json = json.load(file)
print(f"localizadas {len(cartas_json)}")
print(cartas_json[0])

# criar a instancia de carta clow para cada carta
cartas_registros = []
for carta in cartas_json:
    registro = Cartas(nome=carta["nome"], descricao=carta["descricao"], imagem=carta["imagem"])
    cartas_registros.append(registro)
print(f"Serão criadas {len(cartas_registros)} cartas")
print(cartas_registros[0])

# salvar no banco
with Session(engine) as session:
    session.add_all(cartas_registros)
    session.commit()
print("Cartas salvas com sucesso")


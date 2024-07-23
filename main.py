from flask import Flask, render_template, request
from flask import redirect
from sqlalchemy.orm import Session
from modelos import *
from sqlalchemy import func

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/listacartas", methods=["GET"])
def listacartas():
    with Session(engine) as session:
        cartas = session.query(Cartas).all()
    return render_template("listacartas.html", cartas=cartas)


@app.route("/listacartas/<carta_id>", methods=["GET"])
def detalhe_carta(carta_id):
    with Session(engine) as session:
        carta = session.query(Cartas).filter(Cartas.id == carta_id).first()
    return render_template("detalhe_carta.html", carta=carta)


@app.route("/pesquisar", methods=["POST"])
def pesquisar():
    nome_carta = request.form.get("nome_carta")
    with Session(engine) as session:
        carta = session.query(Cartas).filter(func.upper(Cartas.nome) == nome_carta.upper()).first()
    return redirect(f"/listacartas/{carta.id}")


app.run(debug=True)

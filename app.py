
from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import pandas as pd
import os

app = Flask(__name__)
DB_NAME = 'estoque.db'

def conectar():
    return sqlite3.connect(DB_NAME)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categoria/<categoria>')
def categoria(categoria):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nome, categoria, quantidade_atual, estoque_minimo, unidade_medida, preco_compra FROM produtos WHERE categoria = ?",
            (categoria,)
        )
        produtos = cursor.fetchall()
    return render_template('index.html', produtos=produtos, categoria=categoria)

@app.route('/entrada', methods=['GET', 'POST'])
def entrada():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = float(request.form['quantidade'])
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET quantidade_atual = quantidade_atual + ? WHERE nome = ?", (quantidade, nome))
            conn.commit()
        return redirect('/')
    with conectar() as conn:
        cursor = conn.cursor()
        categoria = request.args.get('categoria')
        if categoria:
            cursor.execute("SELECT nome FROM produtos WHERE categoria = ?", (categoria,))
        else:
            cursor.execute("SELECT nome FROM produtos")
        produtos = cursor.fetchall()
    return render_template('entrada.html', produtos=produtos)

@app.route('/saida', methods=['GET', 'POST'])
def saida():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = float(request.form['quantidade'])
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET quantidade_atual = MAX(quantidade_atual - ?, 0) WHERE nome = ?", (quantidade, nome))
            conn.commit()
        return redirect('/')
    with conectar() as conn:
        cursor = conn.cursor()
        categoria = request.args.get('categoria')
        if categoria:
            cursor.execute("SELECT nome FROM produtos WHERE categoria = ?", (categoria,))
        else:
            cursor.execute("SELECT nome FROM produtos")
        produtos = cursor.fetchall()
    return render_template('saida.html', produtos=produtos)

@app.route('/alerta')
def alerta():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome, categoria, quantidade_atual, estoque_minimo, unidade_medida, preco_compra FROM produtos WHERE quantidade_atual < estoque_minimo")
        produtos = cursor.fetchall()
    return render_template('alerta.html', produtos=produtos)

@app.route('/exportar')
def exportar():
    with conectar() as conn:
        df = pd.read_sql_query(
            "SELECT nome, categoria, quantidade_atual, estoque_minimo, unidade_medida, preco_compra FROM produtos WHERE quantidade_atual < estoque_minimo",
            conn
        )
    path = os.path.join("export-itens-abaixo-minimo.xlsx")
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
db = SQLAlchemy(app)

app.secret_key = 'chave_secreta_segura'  # pode ser qualquer string segura


# Modelo de Livro
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(300), nullable=False)

# Rota principal com paginação
@app.route('/')
def home():
    pagina = request.args.get('page', 1, type=int)
    por_pagina = 6

    livros = Livro.query.paginate(page=pagina, per_page=por_pagina)
    return render_template('index.html', livros=livros)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        imagem = request.form.get('imagem')

        if not titulo or not imagem:
            flash('Preencha todos os campos!', 'erro')
            return redirect(url_for('adicionar'))

        novo_livro = Livro(titulo=titulo, imagem=imagem)
        db.session.add(novo_livro)
        db.session.commit()
        flash('Livro adicionado com sucesso!', 'sucesso')
        return redirect(url_for('home'))

    return render_template('adicionar.html')

# Rodar app
if __name__ == '__main__':
    app.run(debug=True)

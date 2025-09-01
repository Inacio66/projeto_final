from app import app, db, Livro

# Usar o contexto da aplicação
with app.app_context():
    # Criar as tabelas
    db.create_all()

    # Inserir livros
    livros_exemplo = [
        Livro(titulo="Casais inteligentes enriquecem juntos", imagem="https://m.media-amazon.com/images/I/71w3iodHVML._UF1000,1000_QL80_.jpg"),
        Livro(titulo="Finanças corporativas", imagem="https://www.livrariasenacceara.com.br/wp-content/uploads/2020/09/Finan%C3%A7as-Corporativas-Teoria-e-Pr%C3%A1tica.jpg"),
        Livro(titulo="Precisa dar certo", imagem="https://m.media-amazon.com/images/I/81Dm4ftnlGL.jpg"),
        Livro(titulo="O poder da ação nas finanças", imagem="https://m.media-amazon.com/images/I/719QAitbRlL._UF350,350_QL80_.jpg"),
    ]

    db.session.bulk_save_objects(livros_exemplo)
    db.session.commit()

    print("Banco criado e livros inseridos com sucesso!")

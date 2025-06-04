from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Usuario, Base


engine = create_engine('sqlite:///banco_de_dados.db')
Base.metadata.create_all(engine)  

Session = sessionmaker(bind=engine)
session = Session()

def criar_usuario(nome: str, idade: int) -> Usuario:
    #Criar novo usuário
    novo_usuario = Usuario(nome=nome, idade=idade)
    #Adicionar a sessão
    session.add(novo_usuario)
    #Salvar as alterações
    session.commit()
    return novo_usuario

def obter_usuarios() -> list[Usuario]:
    Usuarios = session.query(Usuario).all()
    return Usuarios

def obter_usuario_por_nome(nome: str) -> list[Usuario]:
    #Buscar usuários pelo nome
    usuarios = session.query(Usuario).filter_by(nome=nome).all()
    return usuarios

if __name__ == "__main__":
    print("Bem-vindo ao sistema de banco de dados!")
    novo_usuario = criar_usuario("João", 30)
    print(novo_usuario)

    #Imprime todos os usuários
    print("Usuários cadastrados:")
    for usuario in obter_usuarios():
        print(usuario)
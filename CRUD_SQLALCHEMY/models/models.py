from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    """
    Classe que representa a tabela 'usuarios' no banco de dados.
    Atributos:
        id (int): ID do usuario(chave primária).
        nome (str): Nome do usuário.
        idade (int): Idade do usuário.
    """
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<id (ID='{self.id}'), Usuario(nome='{self.nome}', idade={self.idade})>"

# Conectar ao banco
engine = create_engine('sqlite:///banco_de_dados.db')
Base.metadata.create_all(engine)
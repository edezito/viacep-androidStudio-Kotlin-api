from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

#CLASSES DO BD
class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    turno = db.Column(db.String(10), nullable=False)

    alunos = db.relationship('Aluno', back_populates='turma')

    def __repr__(self):
        return f'<Turma {self.nome}>'

class Aluno(db.Model):
    __tablename__ = 'alunos' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(9), nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)  
    nota_segundo_semestre = db.Column(db.Float, nullable=False)  
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)

    turma = db.relationship('Turma', back_populates='alunos')

    def __repr__(self):
        return f'<Aluno {self.nome}>'
    
class AlunoOutput(db.Model):
    __tablename__ = 'alunos_output'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(9), nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)

    aluno = db.relationship('Aluno', back_populates='alunos_output')

    def __repr__(self):
        return f'<AlunoOutput {self.nome}>'
    
class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(9), nullable=False)
    disciplina = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Professor {self.nome}>'
    
class ProfessorOutput(db.Model):
    __tablename__ = 'professores_output'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)  # Idade do professor
    data_nascimento = db.Column(db.String(9), nullable=False)
    disciplina = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<ProfessorOutput {self.nome}>'
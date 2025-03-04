from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import conectar

#INSTANCIANDO FLASK
app = Flask(__name__)
app.secret_key = "projeto-gestao_escolar"


#INSTANCIANDO DB - 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:Tim@o2812@localhost:3306/gestao_escolar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from postgres import psycopg2


app = Flask(__name__)

app.config['SECRET_KEY'] = "somekey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgresql:1@localhost:5432/PostgreSQL_15'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	role = db.Column(db.Integer)
	name = db.Column(db.String(50))
	surename = db.Column(db.String(50))
	password = db.Column(db.String(80))

api = Api()


@app.route()
def 



api.init_app(app)

if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")
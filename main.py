from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
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

#вход в личный кабинет
@app.route('/user', methods=['GET'])
def get_user_info():
	return ""

#регистрация
@app.route('/user', methods=['GET'])
def create_user():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method = 'sha256')
	
	new_user = User(id=data['id'], name = data['name'], surename = data['surename'], 
		password = hashed_password, role = data['role'])

	try:
		db.session.add(new_user)
		db_session.commit()
		return jsonify({"message": 'Success!'})
	except:
		return jsonify({"message": 'Failed!'})



api.init_app(app)

if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")
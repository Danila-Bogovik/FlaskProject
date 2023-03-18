from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from postgres import psycopg2
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


app = Flask(__name__)

app.config['SECRET_KEY'] = "somekey"
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/USERS'



jwt = JWTManager(app)
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	role = db.Column(db.Integer)
	name = db.Column(db.String(50))
	surename = db.Column(db.String(50))
	password = db.Column(db.String(80))

api = Api()

#вход в личный кабинет
@app.route('/profile', methods=['GET'])
def get_user_info():

	users = User.query.all()

	user_data = {}

	for user in users:
		user_data['id'] = user.id
		user_data['role'] = user.role
		user_data['name'] = user.name
		user_data['surename'] = user.surename
		user_data['password'] = user.password

	return jsonify(user_data)

#регистрация
@app.route('/register', methods=['POST'])
def create_user():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method = 'sha256')
	
	new_user = User(id=data['id'], name = data['name'], surename = data['surename'], 
		password = hashed_password, role = data['role'])

	db.session.add(new_user)
	db.session.commit()

	access_token = create_access_token(identity = data['username'])
	refresh_token = create_refresh_token(identity = data['username'])
	return "++"


# вход в систему
@app.route('/login', methods=['POST'])
def user_login():
	return ""



api.init_app(app)

if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")
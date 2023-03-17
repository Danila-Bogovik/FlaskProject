from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from postgres import psycopg2
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt



app = Flask(__name__)

app.config['SECRET_KEY'] = "somekey"
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgresql:1@localhost:5432/PostgreSQL_15'


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
	return ""

#регистрация
@app.route('/register', methods=['POST'])
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


# вход в систему
@app.route('/login', methods=['POST'])
def user_login():
	return ""



api.init_app(app)

if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")
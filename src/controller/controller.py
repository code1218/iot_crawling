
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/pymysql_study'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '427822261c708160050e5f77e0df29f33664e3b8656bf6373cf939cff3c3d446456de28e64049838cd08f0fa48d996c3513312af32629e96a0b82f7097712a616f40d8891c23d325c5668d843a029c3dc05dbe71d4323f436029f1f328c8e53201e6dee152a5fd3566a54a5aa4dd564e39ab10d3914dfe06d058f70dbda61f4cef7ed43d99bbd7380142838b1d4b14d63d4332d6b31faf1e8d74f087e99a0fdd03119f5b2b48836cc4f59f9c084ec927497ced2e47616f115840035b11f527c501ffd2d6004a904806298b046e6278e4b7f9c479cc9c3a373051be8afdcb8543602fcbfcfef5c5be4672437ff1ad2a017dd948a0e9929b10e528efae190185d8'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

with app.app_context():
    db.create_all()

@app.route("/signup", methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']
    name = data['name']
    email = data['email']

    if User.query.filter_by(username=username).first():
        return jsonify({'message': '이미 사용중인 사용자이름입니다.'}), 400

    hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')
    newUser = User(username=username, password=hashedPassword, name=name, email=email)
    db.session.add(newUser)
    db.session.commit()


    return jsonify(user=newUser), 201

@app.route("/print", methods=['GET'])
def printTest():
    print('test')
    return jsonify(message='test입니다'), 200
@app.route("/signin", methods=['POST'])
def signin():
    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id, fresh=True)
        return jsonify(access_token=access_token)
    return jsonify(message='Invalid username or password'), 401




if __name__ == '__main__':
    app.run(debug=True)
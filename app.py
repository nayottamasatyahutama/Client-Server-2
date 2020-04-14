from flask_restful import Resource, Api
from flask import Flask, Response, json, jsonify, request, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/kampuss'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


# Nayottama Satya Hutama
# 18090004
# 4C


# materi pertemuan 3
@app.route('/')
def hello_world():
    return 'Selamat datang'


@app.route('/admin/')
def admin_page():
    return 'Ini adalah halaman admin'
# materi pertemuan tiga berakhir di sini

# materi pertemuan 4


class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/helloworld')
# materi pertemuan 4 berakhir di sini


# materi pertemuan 5
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def get_all_users():
        return User.query.all()


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/user/", methods=["GET"])
def get_user():
    all_users = User.get_all_users()
    result = users_schema.dump(all_users)
    return jsonify(result)

# materi pertemuan 5 berakhir di sini


if __name__ == '__main__':
    app.run()

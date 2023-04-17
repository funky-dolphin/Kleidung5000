from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User

app = Flask(__name__)
app.secret_key = b'\xfe\x97\xb3\xc2h\x0b\xd5\xb7\xbbIR\x80b?\xca\xb0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
api = Api(app)

db.init_app(app)

class Login(Resource):

    def post(self):
        user = User.query.filter(
            User.email_address == request.get_json()['email_address']
        ).first()
# Unsure if these 'user_id' will be this or just ID based on our models
        session['user_id'] = user.id
        return user.to_dict()

api.add_resource(Login, '/login')

class CheckSession(Resource):

    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(CheckSession, '/check_session')

class Logout(Resource):

    def delete(self):
        session['user_id'] = None
        return {'message': '204: No Content'}, 204

api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# b'\xfe\x97\xb3\xc2h\x0b\xd5\xb7\xbbIR\x80b?\xca\xb0'  
    

from flask import request, make_response, jsonify, session
from flask_restful import Resource, Api
from models import db, User
from config import app, bcrypt


api = Api(app)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(
                name = data['name'],
                username = data['username'],
                email_address = data['email_address'],
                paypal_address = data['paypal_address'],
                zipcode = data['zipcode'],
                password_hash = data['_password_hash']
            )
        
        db.session.add(new_user)
        db.session.commit()
        
        response = make_response(new_user.to_dict(), 200)
        return response

api.add_resource(Signup, '/signup')

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        user = User.query.filter(User.username == username).first()

        password = data['password']

        if not user:
            return {'error': 'Invalid username or password'}, 401

        if user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200

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

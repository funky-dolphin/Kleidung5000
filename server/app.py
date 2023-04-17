from flask import request, make_response, jsonify, session
from flask_restful import Resource, Api
from models import db, User
from config import app, bcrypt
from models import Item

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

class Items(Resource):
    def get(self):
        items = Item.query.all()
        items_dict = [item.to_dict() for item in items]
        return items_dict, 200
    
    def post(self):
        data = request.get_json()
        new_item = Item(
            condition = data['condition'],
            image = data['image'], 
            color = data['color'], 
            name = data['name'], 
            price = data['price'], 
            for_sale = data['for_sale'], 
            owner_id = data['owner_id'], 
            type_id = data['type_id'], 
            subtype_id = data['subtype_id'], 
            size_id = data['size_id'], 
            brand_id = data['brand_id']
        )
        db.session.add(new_item)
        db.session.commit()
        return make_response(new_item.to_dict(), 201)
    
api.add_resource(Items, '/items')

class ItemsById(Resource):
    def get(self, id):
        item = Item.query.filter_by(id = id).first()
        return item.to_dict(), 200
    
    def patch(self, id):
        item = Item.query.filter_by(id = id).first()
        data = request.get_json()
        for attr in data:
            setattr(item, attr, data[attr])
        db.session.add(item)
        db.session.commit()
        item_dict = item.to_dict()

        return make_response(item_dict, 202)
    
    def delete(self, id):
        item = Item.query.filter_by(id = id).first()
        db.session.delete(item)
        db.session.commit()
    
api.add_resource(ItemsById, '/items/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)    

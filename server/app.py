from flask import request, make_response, jsonify, session
from flask_restful import Resource, Api
from models import db, User, Type, SubType, Brand, Transaction, Size, Message
from config import app, bcrypt
from models import Item

api = Api(app)

class Signup(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

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

class Users_By_Id(Resource):
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()
        
        if '_password_hash' in data:
            password_hash = bcrypt.generate_password_hash(data['_password_hash'].encode('utf-8'))
            data['_password_hash'] = password_hash.decode('utf-8')
        
        for attr in data:
            setattr(user, attr, data[attr])
        
        db.session.add(user)
        db.session.commit()

        response = make_response(user.to_dict(), 202)
        return response

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({
                "error": "User not found"
            }, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response(
            {"User":"deleted"}, 201
        )
    
api.add_resource(Users_By_Id, '/users/<int:id>')

class Types(Resource):
    def get(self):
        types = Type.query.all()
        type_dict = [type.to_dict()for type in types]
        return make_response(
            type_dict,
            200
        )
    
api.add_resource(Types, '/types')

class SubTypes(Resource):
    def get(self):
        subtypes = SubType.query.all()
        subtype_dict = [subtype.to_dict()for subtype in subtypes]
        return make_response(
            subtype_dict,
            200
        )
    
api.add_resource(SubTypes, '/subtypes')

class Sizes(Resource):
    def get(self):
        sizes = Size.query.all()
        size_dict = [size.to_dict() for size in sizes]
        return make_response(
            size_dict,
            200
        )
    
api.add_resource(Sizes, '/sizes')

class Brands(Resource):
    def get(self):
        brands = Brand.query.all()
        brand_dict = [brand.to_dict() for brand in brands]
        return make_response(
            brand_dict,
            200
        )
    
api.add_resource(Brands, '/brands')

class Transactions(Resource):
    def get(self):
        transactions = Transaction.query.all()
        transaction_dict = [transaction.to_dict() for transaction in transactions]
        return make_response(
            transaction_dict,
            200
        )
    
api.add_resource(Transactions, '/transactions')

class Messages(Resource):
    def get(self):
        messages = Message.query.all()
        message_dict = [message.to_dict() for message in messages]
        return make_response(
            message_dict,
            200
        )
    def post(self):
        data = request.get_json()
        try:
            message = Message(
                message=data['message']
            )

            db.session.add(message)
            db.session.commit()
        except Exception as e:
            message = {
                'errors': [e.__str__()]
            }
            return make_response(
                message,
                422
            )
        
        response = make_response(
            message.to_dict(),
            201
        )
        return response

api.add_resource(Messages, '/messages')

class Messages_By_Id(Resource):
    def patch(self, id):
        message = Message.query.filter_by(id=id).first()
        data = request.get_json()
        for attr in data:
            setattr(message, attr, data[attr])
        db.session.add(message)
        db.session.commit()

        response = make_response(message.to_dict(), 202)
        return response

api.add_resource(Messages_By_Id, '/messages/<int:id>')

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

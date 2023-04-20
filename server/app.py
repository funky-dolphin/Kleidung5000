from flask import request, make_response, jsonify, session
from flask_restful import Resource, Api
from models import db, User, Type,Item, SubType, Brand, Transaction, Size, Message, FavoriteItem
from config import app, bcrypt


api = Api(app)
app.secret_key = 'c5ca72e12d6aac51f6bb8544'

# @app.before_request
def checkSession():
    print(session.get("user_id")," is the user id session")
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
        print("Received data:", data)
        username = data['username']
        user = User.query.filter(User.username == username).first()

        password = data['password']

        if not user:
            return {'error': 'Invalid username or password'}, 401

        if user.authenticate(password):
            session['user_id'] = user.id
            print(session.get('user_id')," is the session data")
            return user.to_dict(), 200
        

api.add_resource(Login, '/login')

class CheckSession(Resource):

    def get(self):
        print(session.get('user_id'),"this is the session data")
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(CheckSession, '/check_session')
# AUTHORIZED
class Logout(Resource):

    def delete(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        session['user_id'] = None
        return {'message': '204: No Content'}, 204

api.add_resource(Logout, '/logout')
# AUTHORIZED
class Users_By_Id(Resource):
    def patch(self, id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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

class TypesById(Resource):
    def get(self, id):
        type = Type.query.filter_by(id = id).first()
        return type.to_dict(), 200
api.add_resource(TypesById, '/types/<int:id>')

class SubTypes(Resource):
    def get(self):
        subtypes = SubType.query.all()
        subtype_dict = [subtype.to_dict()for subtype in subtypes]
        return make_response(
            subtype_dict,
            200
        )
    
api.add_resource(SubTypes, '/subtypes')

class SubTypesById(Resource):
    def get(self, id):
        subtype = SubType.query.filter_by(id = id).first()
        return subtype.to_dict(), 200
api.add_resource(SubTypesById, '/subtypes/<int:id>')

class Sizes(Resource):
    def get(self):
        sizes = Size.query.all()
        size_dict = [size.to_dict() for size in sizes]
        return make_response(
            size_dict,
            200
        )
    
api.add_resource(Sizes, '/sizes')

class SizesById(Resource):
    def get(self, id):
        size = Size.query.filter_by(id = id).first()
        return size.to_dict(), 200
api.add_resource(SizesById, '/sizes/<int:id>')

class Brands(Resource):
    def get(self):
        brands = Brand.query.all()
        brand_dict = [brand.to_dict() for brand in brands]
        return make_response(
            brand_dict,
            200
        )
    
api.add_resource(Brands, '/brands')

class BrandsById(Resource):
    def get(self, id):
        brand = Brand.query.filter_by(id = id).first()
        return brand.to_dict(), 200
api.add_resource(BrandsById, '/brands/<int:id>')
# AUTHORIZED
class Transactions(Resource):
    def get(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        transactions = Transaction.query.all()
        transaction_dict = [transaction.to_dict() for transaction in transactions]
        return make_response(
            transaction_dict,
            200
        )
    
api.add_resource(Transactions, '/transactions')
# AUTHORIZED
class Messages(Resource):
    def get(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        messages = Message.query.all()
        message_dict = [message.to_dict() for message in messages]
        return make_response(
            message_dict,
            200
        )
    def post(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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
# AUTHORIZED
class Messages_By_Id(Resource):
    def patch(self, id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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
        items_dict = [item.to_dict(rules=('size', 'brand')) for item in items]
        return items_dict, 200
  
    def post(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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
    # AUTHORIZATION
    def patch(self, id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        item = Item.query.filter_by(id = id).first()
        data = request.get_json()
        for attr in data:
            setattr(item, attr, data[attr])
        db.session.add(item)
        db.session.commit()
        item_dict = item.to_dict()

        return make_response(item_dict, 202)
    #AUTHORIZED 
    def delete(self, id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        item = Item.query.filter_by(id = id).first()
        db.session.delete(item)
        db.session.commit()
    
api.add_resource(ItemsById, '/items/<int:id>')
# AUTHORIZED
class ItemsByOwner(Resource):
    def get(self,id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        items = Item.query.filter_by(owner_id = id).all()
        items_dict = [item.to_dict() for item in items]
        return make_response(items_dict,200)

api.add_resource(ItemsByOwner, '/itemsbyowner/<int:id>')
    
class ItemsByType(Resource):
    def get(self,id):
        items = Item.query.filter_by(type_id = id).all()
        items_dict=[item.to_dict(rules=('size', 'brand')) for item in items]
        return make_response(items_dict, 201)
api.add_resource(ItemsByType, '/itemsbytype/<int:id>')

class ItemsBySubType(Resource):
    def get(self,type_id, subtype_id):
        items = Item.query.filter_by(type_id=type_id, subtype_id=subtype_id).all()
        items_dict=[item.to_dict(rules=('size', 'brand')) for item in items]
        return make_response(items_dict, 201)
api.add_resource(ItemsBySubType, '/itemsbysubtype/<int:type_id>/<int:subtype_id>')
    
# AUTHORIZED
class FavoriteItems(Resource):
    def post(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        data = request.get_json()
        favorite_item = FavoriteItem(
            item_id = data['item_id'],
            user_id = data['user_id'], 
        )
        db.session.add(favorite_item)
        db.session.commit()
        return make_response(favorite_item.to_dict(), 201)
api.add_resource(FavoriteItems, '/favoriteitems')
# AUTHORIZED
class FavoriteItemsByOwner(Resource):
    def get(self,id):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
        items = FavoriteItem.query.filter_by(user_id = id).all()
        items_dict = [item.to_dict() for item in items]
        return make_response(items_dict,200)
    
api.add_resource(FavoriteItemsByOwner, '/favoriteitemsbyowner/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)    

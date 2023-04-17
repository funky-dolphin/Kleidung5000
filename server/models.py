
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt, db, app

app.secret_key = b'\xfe\x97\xb3\xc2h\x0b\xd5\xb7\xbbIR\x80b?\xca\xb0'

class User(db.Model, SerializerMixin):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    username=db.Column(db.String, nullable=False)
    email_address=db.Column(db.String)
    paypal_address=db.Column(db.String)
    zipcode=db.Column(db.Integer)
    _password_hash = db.Column(db.String, nullable=False)

    transactions = db.relationship('Transaction', back_populates = 'users')
    messages = db.relationship('Message', back_populates = 'users')

    serialize_rules = ('-transactions.users', '-messages.users')

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
            password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
            self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
         return bcrypt.check_password_hash(
             self._password_hash, password.encode('utf-8'))



class Item(db.Model, SerializerMixin): 
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.Integer, db.CheckConstraint( '10 >= condition >= 1' ), 
                     nullable = False  )
    image = db.Column(db.String)
    color = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    for_sale=db.Column(db.Boolean)
    owner_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    subtype_id = db.Column(db.Integer, db.ForeignKey('subtypes.id'))
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))

    type = db.relationship('Type', back_populates = 'items')
    subtype = db.relationship('SubType', back_populates ="items")

    serialize_rules = ('-type', '-subtype', '-brand', '-size')
    
class Type(db.Model, SerializerMixin):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    items = db.relationship('Item', back_populates='type')
    subtype = db.relationship('SubType', back_populates= 'type')

    serialize_rules = ('-items', '-subtype')
    
    def __repr__(self):
        return f'Type: {self.type}'

class SubType(db.Model, SerializerMixin):
    __tablename__ = 'subtypes'

    id = db.Column(db.Integer, primary_key=True)
    subtype = db.Column(db.String)

    type_id = db.Column(db.String, db.ForeignKey('types.id'))

    type = db.relationship('Type', back_populates = 'subtype')
    items = db.relationship('Item', back_populates='subtype')

    serialize_rules = ('-type', '-items')

    def __repr__(self):
        return f'subtype: {self.subtype}'

class Size(db.Model, SerializerMixin):
    __tablename__ = 'sizes'

    id=db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String)

    items = db.relationship('Item', backref='size')

    serialize_rules = ('-items',)

    def __repr__(self):
        return f'Size: {self.size}'

class Brand(db.Model, SerializerMixin):
    __tablename__ = 'brands'

    id=db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)

    items = db.relationship('Item', backref='brand')

    serialize_rules = ('-items',)

    def __repr__(self):
        return f'Brand: {self.brand}'
    
class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'

    id=db.Column(db.Integer, primary_key=True)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    buyer_id = db.Column(db.Integer, default=None)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    price = db.Column(db.Float, db.ForeignKey('items.price'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    users = db.relationship('User', back_populates = 'transactions')

    serialize_rules = ('-users',)


class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id=db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    user_1 = db.Column(db.Integer, default=None)
    user_2 = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('User', back_populates = 'messages')

    serialize_rules = ('-users',)



    



    
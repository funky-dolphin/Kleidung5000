from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    email_address=db.Column(db.String)
    paypal_address=db.Column(db.String)
    zipcode=db.Column(db.Integer)

    transactions = db.relationship('Transaction', back_populates = 'users')
    messages = db.relationship('Message', back_populates = 'users')


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
    type_id = db.Column(db.String, db.ForeignKey('types.id'))
    subtype_id = db.Column(db.String, db.ForeignKey('subtypes.id'))
    size_id = db.Column(db.String, db.ForeignKey('sizes.id'))
    brand_id = db.Column(db.String, db.ForeignKey('brands.id'))

    type = db.relationship('Type', back_populates = 'items')
    # subtype = db.relationship('Subtype', back_populates='items')
    subtypes = association_proxy('Type', 'subtypes')

class Type(db.Model, SerializerMixin):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    items = db.relationship('Item', back_populates='type')
    subtypes = db.relationship('SubType', back_populates= 'type')

class SubType(db.Model, SerializerMixin):
    __tablename__ = 'subtypes'

    id = db.Column(db.Integer, primary_key=True)
    subtype = db.Column(db.String)

    type_id = db.Column(db.String, db.ForeignKey('types.id'))

    type = db.relationship('Type', back_populates = 'subtypes')
    # items = db.relationship('Item', back_populates='subtype')

class Size(db.Model, SerializerMixin):
    __tablename__ = 'sizes'

    id=db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String)

    items = db.relationship('Item', backref='size')

class Brand(db.Model, SerializerMixin):
    __tablename__ = 'brands'

    id=db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)

    items = db.relationship('Item', backref='brand')


class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'

    id=db.Column(db.Integer, primary_key=True)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    buyer_id = db.Column(db.Integer, default=None)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    price = db.Column(db.Float, db.ForeignKey('items.price'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    users = db.relationship('User', back_populates = 'transactions')


class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id=db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    user_1 = db.Column(db.Integer, default=None)
    user_2 = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('User', back_populates = 'messages')



    



    
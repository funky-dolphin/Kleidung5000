from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_cors import CORS
import redis 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['COORS_HEADERS']= 'Content_Type'
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xfe\x97\xb3\xc2h\x0b\xd5\xb7\xbbIR\x80b?\xca\xb0'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER']= True
app.config['SESSION_REGIS'] = redis.from_url("redis://127.0.0.1:5555")
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False


app.json.compact = False

# app.secret_key = b'\xfe\x97\xb3\xc2h\x0b\xd5\xb7\xbbIR\x80b?\xca\xb0'
migrate = Migrate(app, db)
db.init_app(app)


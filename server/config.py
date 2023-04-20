from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_session import Session

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['COORS_HEADERS']= 'Content_Type'
bcrypt = Bcrypt(app)
CORS(app)

# app.config['SESSION_TYPE']='filesystem'
# app.config['SESSION_FILE_DIR'] = './.flask_session/'
# app.config['SESSION_FILE_THRESHOLD'] = 100
# app.config['SESSION_PERMANENT'] = False
app.config['SECRET_KEY']='c5ca72e12d6aac51f6bb8544'
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
# Session(app)


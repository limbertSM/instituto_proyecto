"""import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave_secreta_predeterminada"
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'instituto_sis'
    MYSQL_CURSORCLASS = 'DictCursor'"""


import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-segura'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/instituto_sis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

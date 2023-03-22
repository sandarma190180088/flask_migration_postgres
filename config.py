import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    HASHIDS_SALT = 'secret!'
    JWT_SECRET_KEY = 'fasism123'

    SQLALCHEMY_DATABASE_URI= f"postgresql://xmzkjvkvsjowvj:bc7db9c460fb505b7805fbcadd540a106f6018ba21dee6d5e73e9723df31f96b@ec2-3-208-74-199.compute-1.amazonaws.com:5432/d2p2oee8tklnjc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    

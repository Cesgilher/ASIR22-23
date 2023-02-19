
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1asir@informatica.iesquevedo.es:3333/cesar"
    
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY="cesar"
    DEBUG = True
    TESTING = True


# Configuration for Production:

class Config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    
    
class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    DEBUG = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'thisisprojectpassword'
    SECRET_KEY = 'shouldbekeptSecretforinternalreasons'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'  #Default
    SECURITY_TOKEN_MAX_AGE = 36000
    
    
    #Cache Specific...
    
    WTF_CSRF_ENABLED = False
    
    
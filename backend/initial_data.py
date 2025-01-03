from flask import current_app as app
from models import db
from flask_security import SQLAlchemySessionUserDatastore, hash_password


with app.app_context():
    db.create_all()
    
    userdatastore: SQLAlchemySessionUserDatastore = app.security.datastore
    userdatastore.find_or_create_role(name = 'admin', description = 'superuser')
    userdatastore.find_or_create_role(name = 'user', description = 'user')
    
    if(not userdatastore.find_user(email = 'admin@project.com')):
        userdatastore.create_user(email = 'admin@project.com', password = hash_password('1234'), roles = ['admin'])
    if(not userdatastore.find_user(email = 'user01@project.com')):
        userdatastore.create_user(email = 'user01@project.com', password = hash_password('1234'), roles = ['user'])
        
    db.session.commit()
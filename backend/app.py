from flask import Flask
from config import LocalDevelopmentConfig
from models import db, User, Role
from flask_caching import Cache
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_cors import CORS
from celery_tasks.celery_factory import celery_init_app



def createApp():
    app = Flask(
        __name__,
        template_folder = "../frontend",
        static_folder = "../frontend",
        static_url_path = "/static",
    )
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config.from_object(LocalDevelopmentConfig)
    
    #model initialization
    db.init_app(app)
    
    # Cache Initialization
    
    cache = Cache(app)
    app.cache = cache
    
    
    # Flask Security
    
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, datastore=datastore, register_blueprint=False)

    app.app_context().push()
    
    # Restful Initialization
    from resources import api
    api.init_app(app)
    
    return app

app = createApp()
celery_app = celery_init_app(app)

import initial_data
import routes


if __name__ == '__main__':
    app.run()

    
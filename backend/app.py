from flask import Flask
from config import LocalDevelopmentConfig
from models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_cors import CORS



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
    
    # Restful Initialization
    from resources import api
    api.init_app(app)
    
    # Flask Security
    
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, datastore=datastore, register_blueprint=False)

    app.app_context().push()
    
    return app

app = createApp()
import initial_data
import routes


if __name__ == '__main__':
    app.run()

    
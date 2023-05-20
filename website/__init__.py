from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from .views import views
    from .auth  import auth
    from .socketio_functions import socketio_functions
    from .database import setup_database, cleanup_database
    from .databaseChat import setup_databaseChat
    from .databaseMessages import setup_databaseMessages
    # Register blueprints
    # cleanup_database()
    setup_database() # Create tables such as user table
    setup_databaseChat()
    setup_databaseMessages()
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,  url_prefix='/')
    app.register_blueprint(socketio_functions, url_prefix='/')

    return app
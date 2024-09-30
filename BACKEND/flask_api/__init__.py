from flask import Flask
from flask_api.config import Config
from flask_api.extensions import db, migrate, init_extensions, user_datastore
from flask_api.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_extensions(app) 
    app.register_blueprint(main) 
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
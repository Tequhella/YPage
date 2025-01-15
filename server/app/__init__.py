from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Utilisez SQLite pour commencer
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Extensions
    db.init_app(app)
    CORS(app)

    # Enregistrement des routes
    from app.routes import bp as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
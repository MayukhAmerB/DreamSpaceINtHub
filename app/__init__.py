from flask import Flask

def create_app():
    app = Flask(__name__)
    # Basic configuration
    app.config['SECRET_KEY'] = 'dev'
    app.config['DEBUG'] = True

    from .routes import main
    app.register_blueprint(main)

    return app

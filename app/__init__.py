from flask import Flask

from config import Config
from app.extension import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation Flask extensions here
    db.init_app(app)

    # Enregistrement blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/test/')
    def test_page():
        return 'Hello World!'


    return app
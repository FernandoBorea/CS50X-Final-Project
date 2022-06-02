from flask import Flask
from flask_mail import Mail


mail = Mail()
def init_app():
    # Set up core app
    app = Flask(__name__)
    app.config.from_object('config.Config')
    mail.init_app(app)
    
    with app.app_context():
        # Import app routes
        from .index import routes

        # Register blueprints
        app.register_blueprint(routes.index_bp)

        return app

from flask import Flask

def init_app():
    # Set up core app
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    with app.app_context():
        # Import app routes
        from .index import routes

        # Register blueprints
        app.register_blueprint(routes.index_bp)

        return app

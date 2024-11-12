from flask import Flask

def create_app():
    print("Creating the app!")  # This should be printed in the terminal
    app = Flask(__name__)
    app.config.from_object('config')  # Load configuration

    # Import routes inside the app context
    with app.app_context():
        from . import routes  # Ensure routes are imported here
        routes.init_routes(app)  # Initialize routes

    return app
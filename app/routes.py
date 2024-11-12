from flask import render_template, current_app

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
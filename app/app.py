
def create_app():
    from flask import Flask
    app = Flask(__name__)

    load_modules(app)
    return app


def load_modules(app):
    import app.config as config
    config.init_app(app)

    import app.routes as routes
    routes.init_app(app)

    from app.ext import db
    db.init_app(app)

    from app.producer import producer
    producer.init_app(app)

import os

from flask import Flask

from db import close_db, init_db
from routes import bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["DATABASE"] = os.path.join(app.root_path, "inspections.db")
    if test_config:
        app.config.update(test_config)

    app.teardown_appcontext(close_db)
    app.register_blueprint(bp)

    with app.app_context():
        init_db()
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

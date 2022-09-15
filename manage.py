from flask import Flask

from app import api_bp
from app.main import create_app


app = create_app("dev")
app.register_blueprint(api_bp, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run()

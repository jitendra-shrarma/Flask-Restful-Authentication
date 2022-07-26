# import default modules
from flask import Flask

# import create_app factory function and application blueprint(api_bp)
from app import blueprint
from app.main import create_app


# create app using create_app() function having 'dev' environment
app = create_app('dev')
app.register_blueprint(api_bp, url_prefix="/api/v1")


# run application
if __name__ == "__main__":
    app.run()

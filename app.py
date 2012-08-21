import flask, sys
from db import db
from auth import login_manager, bcrypt
from flask.ext.bcrypt import Bcrypt

# list of modules from whom to register our blueprints
MODULES= [
    'auth',
    'portfolio',
]

def register_extensions(app):
    db.init_app()
    login_manager.setup_app(app)
    bcrypt.init_app(app)

def generate_app(modules=MODULES, register_extensions=register_extensions):
    """
    Generate the app we run
    """
    app = flask.Flask(__name__)
    
    # configure based on chosen environment
    if 'production' == env:
        app.config.from_object('config.Production')
    elif 'test' == env:
        app.config.from_object('config.Testing')
    elif 'development' == env:
        app.config.from_object('config.Development')
    else:
        app.config.from_object('config.Development')
    
    # register extensions
    register_extensions(app)

    # register views from each module
    for module in modules:
        app.register_blueprint(module.views)
        
    return app

# run the app
if __name__ == '__main__':
    env = sys.argv[1]
    app = generate_app(env)
    app.run()

import flask, sys, os
from flaskext.script import Manager, Command, Option
from flask.ext.assets import Environment, Bundle
from db import db

# add app directory to sys path, for imports
root = os.getcwd()
sys.path.append(root)

# set up flask instance
app = flask.Flask(__name__)
app.config.from_object('config.settings')

# create asset bundle
assets = Environment()
js = Bundle('auth.js', 
            'jquery.js',
            'backbone.js',
            'handlebars.js',
            filters='jsmin',
            output='bundle.js')
less = Bundle('bootstrap/less/bootstrap.less',
              'myless.less',
              filters='less', 
              output='bundle.css',
              debug=False)
asset_config = {
    'less_bin' : 'less.js/bin/lessc',
}
bundles = [['js', js], ['css', less]]

# list of modules from whom to register our blueprints
INSTALLED_MODULES= [
    'auth',
    'opportunity',
]

# manager and ommands
manager = Manager(app)

class Run(Command):
    """
    Start the app, with options to control the environment.
    """
    options_list = (
        Option('--development', '-n', dest='development'),
        Option('--test', '-t', dest='test'),
        Option('--production', '-p', dest='production'),
    )

    def run(self, **kwargs):
        # set up additional configuration based on chosen environment
        if 'production' in kwargs.keys():
            app.config.from_object('config.prod')
        elif 'test' in kwargs.keys():
            app.config.from_object('config.test')
        elif 'development' in kwargs.keys():
            app.config.from_object('config.dev')
        else:
            app.config.from_object('config.dev')

        # register asset bundles
        assets.init_app(app)
        for bundle in bundles:
            assets.register(*bundle)
        for option, value in asset_config.iteritems():
            assets.config[option] = value

        # register blueprints
        for module in INSTALLED_MODULES:
            app.register_blueprint(__import__(module).blueprint)

        # register database
        db.init_app(app)

        # start the app!
#        print app.url_map # if you need to see a list of your URLs
        app.run()

manager.add_command('run', Run())

# run the app
if __name__ == '__main__':
    manager.run()

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

from app.controllers.main import main


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize bootstrap theme
    Bootstrap(app)

    # initialize the debug tool bar
    debug_toolbar = DebugToolbarExtension()
    debug_toolbar.init_app(app)

    # register our blueprints
    app.register_blueprint(main)

    return app

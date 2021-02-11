from flask import Flask


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object("config.Config")

    with app.app_context():
        # Include our Routes
        from . import routes  # noqa: F401

        from .dashapp.dashboard import init_dashboard
        from .dashapp2.dashboard2 import init_dashboard_2

        app = init_dashboard(app)
        app = init_dashboard_2(app)

        return app

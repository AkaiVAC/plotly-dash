from flask import current_app as app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.jinja2")


@app.route("/about")
def about():
    return render_template("about.jinja2", about_me="About MYSELF")

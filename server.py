from flask import Flask, render_template, redirect, request, flash, session
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

@app.route('/')
def show_home_page():
    """ Shows the homepage with links for login and registration.
    """
    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')
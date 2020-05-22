from flask import Flask, render_template, redirect, request, flash, session
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = "ABC"



fields = [{
  "tag": "input",
  "name": "first_name",
  "type": "text",
  "human_label": "First Name"
}, {
  "tag": "input",
  "name": "last_name",
  "type": "text",
	"human_label": "Last Name"
}, {
  "tag": "input",
  "name": "email",
  "type": "email",
  "human_label": "Email Address"
}, {
  "tag": "input",
  "name": "phone_number",
  "type": "text",
  "human_label": "Phone Number"
}, {
  "tag": "input",
  "name": "job_title",
  "type": "text",
  "human_label": "Job Title"
}, {
  "tag": "input",
  "name": "date_of_birth",
  "type": "date",
  "human_label": "Date of Birth"
}, {
  "tag": "input",
  "name": "parental_consent",
  "type": "checkbox",
  "human_label": "Parental Consent",
	"conditional": {
		"name": "date_of_birth",
		"show_if": "(value) => {const now = new Date(); return value >= new Date(now.getFullYear() - 13, now.getMonth(), now.getDate());}"
    }
}
]

@app.route('/', methods=["GET"])
def show_home_page():
    """ Shows the homepage with form elements
    """
    return render_template("homepage.html", fields=fields)


@app.route('/register', methods=["POST"])
def register_user_info():
  """generates a clean json from user_info"""

  info = {}

  for field in fields:
    info[field["name"]] = request.form.get(field["name"])

  return jsonify(info)


if __name__ == "__main__":
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')
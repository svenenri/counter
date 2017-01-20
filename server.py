# Create a simple web application that holds a counter that increments every
# time the page is visited. Complete this using session.
# For ninjas: add a +2 button underneath the counter that increments the counter
# by 2 and reloads the page.
# For hackers: add a reset button that will reset the counter to 1

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():

	try:
		session["counter"] += 1
	except:
		session["counter"] = 1

	return render_template("index.html", count = session["counter"])

@app.route("/count", methods=["POST"])
def count():
	req = request.form["alt"]
	if req == "PlusTwo":
		session["counter"] += 1
		return redirect("/")
	elif req == "Reset":
		session["counter"] = 0
		return redirect("/")

app.run(debug = True)

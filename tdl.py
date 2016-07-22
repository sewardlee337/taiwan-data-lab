from flask import Flask, render_template, request, redirect

app = Flask(__name__)				

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html', title='Home')


@app.route("/data")
def datapage():
	return render_template('data.html', title='Data')

@app.route("/thanks")
def thanks():
	return render_template('thanks.html', title='Thanks')

if __name__ == "__main__":
	app.run()

"""
export FLASK_APP=tdl.py
export FLASK_DEBUG=1
flask run
"""


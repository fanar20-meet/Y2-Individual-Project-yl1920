from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)


# routes 
@app.route('/')
def home():
	return render_template("home.html")


@app.route('/signup')
def home():
	return render_template("signup.html")


# @app.route('/body')
# def about():
# 	return render_template("body.html")


# //////////////////////



if __name__ == '__main__':
    app.run(debug=True)

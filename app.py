from flask import Flask, request, redirect, url_for, render_template
from databases import *

app = Flask(__name__)


# routes 

# signin
@app.route('/')
def home():
	return signup()
	# return render_template("home.html")

@app.route('/add', methods=['GET', 'POST'])
def signup():
		if request.method == 'GET':
			return render_template('signup.html')
		else:

			name = request.form['user_name']
			year = request.form['user_year']
			add_user(name,year,0)
			return redirect('/user/' + name)		


@app.route('/body')
def about():
	return render_template("body.html")


@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('user.html', user=query_by_name(user_name))

@app.route('/immune_system')
def Immune():
	return render_template('imm.html')

@app.route('/nervous_system')
def nervous():
	return render_template('nervous.html')

# //////////////////////



if __name__ == '__main__':
    app.run(debug=True)

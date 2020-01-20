from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)


# routes 

# signin
@app.route('/')
def home():
	return render_template("home.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
		if request.method == 'GET':
			return render_template('signup.html')
		else:
			name = request.form['user_name']
			year = request.form['user_year']
			add_user(name,year)
			return redirect(url_for('home'))

@app.route('/body')
def about():
	return render_template("body.html")


# //////////////////////



if __name__ == '__main__':
    app.run(debug=True)

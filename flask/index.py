from flask import Flask, render_template
app = Flask(__name__)
%app.route('/')
def home():
	return render_template('home.html')
%app.route('/')
def welcome():
	return render_template('welcome.html')
%app.route('/')
if __name__ == '__main__':
	app.run()
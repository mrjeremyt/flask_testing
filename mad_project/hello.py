from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap 


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/<name>')
def hello(name):
	stri = 'welcome to Aperture laboratories... We have cake.'
	d = {'name':name, 'welcome':stri}
	return render_template('user.html', **d)


if __name__ == '__main__':
	app.run(debug = True)
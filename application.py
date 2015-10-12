from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return 'This the admin page.'

@app.route('/booth')
def booth():
    return 'This is a booth page'

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

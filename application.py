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

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/<name>/')
def booth(name=None):
    return render_template('booth.html', name=name)


@app.route('/<name>/admin/')
def boothAdmin(name=None):
    return render_template('booth-admin.html', name=name)

@app.route('/<name>/<item>/')
def item(name=None, item=None):
    return render_template('item.html', name=name, item=item)


@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

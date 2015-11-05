from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_model import Base, Items, Booths


app = Flask(__name__)


# Connect to database and create session
engine = create_engine('sqlite:///fleamarket.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def index():
    booths = session.query(Booths).order_by(asc(Booths.name))
    items = session.query(Items).order_by(asc(Items.name))
    return render_template('index.html', booths=booths, items=items)


@app.route('/booths/')
def booths():
    booths = session.query(Booths).order_by(asc(Booths.name))
    return render_template('booths.html', booths=booths)

@app.route('/booths/<name>/')
def booth(name=None):
    return render_template('booth.html', name=name)


@app.route('/<name>/<item>/')
def item(name=None, item=None):
    return render_template('item.html', name=name, item=item)


@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

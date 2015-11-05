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
@app.route('/booths/')
def index():
    booths = session.query(Booths).order_by(asc(Booths.name))
    return render_template('index.html', booths=booths)


@app.route('/booth/<int:booth_id>/')
def booth(booth_id=None):
    booth = session.query(Booths).filter_by(id=booth_id).one()
    items = session.query(Items).filter_by(booth_id=booth_id)
    return render_template('booth.html', booth=booth, items=items)

@app.route('/add/')
def addItem(booth_id = None):
    return render_template('addItem.html')


@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

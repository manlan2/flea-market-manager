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

# Show all booths and link to all items. Home page of app.
@app.route('/')
@app.route('/booths/')
def index():
    ''' Add comment here '''
    booths = session.query(Booths).order_by(asc(Booths.name))
    return render_template('index.html', booths=booths)


# List of all items
@app.route('/items/')
def allItems(booth_id = None):
    ''' Add comment here '''
    items = session.query(Items).order_by(asc(Items.name))
    return render_template('items.html', items=items)


# Show booth items and info
@app.route('/booth/<int:booth_id>/')
def booth(booth_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    items = session.query(Items).filter_by(booth_id=booth_id)
    return render_template('booth.html', booth=booth, items=items)


# Single item view #TODO: this is not working.  No item sent to template?
@app.route('/booth/<int:booth_id>/<int:item_id>/')
def item(booth_id=None, item_id = None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id)
    return render_template('item.html', booth=booth, item=item)


# Add item
@app.route('/booth/<int:booth_id>/new/')
def addItem(booth_id = None):
    ''' This function is used to create new items for a booth.'''
    return render_template('addItem.html')


# Edit item
@app.route('/booth/<int:booth_id>/<int:item_id>/edit/')
def editItem(booth_id = None, item_id = None):
    ''' Add comment here '''
    return render_template('editItem.html')

# Delete item
@app.route('/booth/<int:booth_id>/<int:item_id>/delete/')
def deleteItem(booth_id = None, item_id = None):
    ''' Add comment here '''
    return render_template('deleteItem.html')


@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

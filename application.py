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
    ''' Add comment here ''' #TODO: Add comment
    booths = session.query(Booths).order_by(asc(Booths.name))
    return render_template('index.html', booths=booths)


# List of all items
@app.route('/items/')
def allItems(booth_id = None):
    ''' Add comment here ''' #TODO: Add comment
    items = session.query(Items).order_by(asc(Items.name))
    return render_template('items.html', items=items)

# This section contains the routes and functions to manage booths

# Add a booth
# @app.route('/booth/new/', methods = ['GET', 'POST'])
# def newBooth():
#     ''' Add comment here ''' # TODO: Add comment
#     pass #TODO: finish code


# Edit booth
# @app.route('/booth/booth_id/edit/', methods=['GET', 'POST'])
# def editBooth():
#     ''' Add comment here. ''' #TODO: Add comment
#     pass #TODO: add code


# Delete booth
# @app.route('/booth/booth_id/delete/', methods=['GET', 'POST'])
# def deleteBooth():
#     ''' Add comment here. ''' #TODO: Add comment
#     pass #TODO: add code



# Show booth items and info
@app.route('/booth/<int:booth_id>/')
def booth(booth_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    items = session.query(Items).filter_by(booth_id=booth_id)
    return render_template('booth.html', booth=booth, items=items)

# This section contains the routes and fuctions to manage items

# Single item view #TODO: this is not working.  No item sent to template?
@app.route('/booth/<int:booth_id>/<int:item_id>/')
def item(booth_id=None, item_id = None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id)
    return render_template('item.html', booth=booth, item=item)


# Add item
@app.route('/booth/<int:booth_id>/new/', methods = ['GET', 'POST'])
def addItem(booth_id = None):
    ''' This function is used to create new items for a booth.'''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    if request.method == 'POST':
        pass
    else:
        return render_template('addItem.html', booth=booth)


# Edit item
@app.route('/booth/<int:booth_id>/<int:item_id>/edit/')
def editItem(booth_id = None, item_id = None):
    ''' Add comment here '''
    if request.method == 'POST':
        pass
    else:
        return render_template('editItem.html', item=item, booth=booth)

# Delete item
@app.route('/booth/<int:booth_id>/<int:item_id>/delete/')
def deleteItem(booth_id = None, item_id = None):
    ''' Add comment here '''
    return render_template('deleteItem.html')


# JSON API

# @app.route('/booth/<int:booth_id>/json/')
#
# @app.route('booths/json')

@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='True', host='0.0.0.0', port=8000)

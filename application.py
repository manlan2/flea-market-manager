from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import flash
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_model import Base, Items, Booths
import random
import string


app = Flask(__name__)



# Connect to database and create session
engine = create_engine('sqlite:///fleamarket.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all booths and link to all items. Home page of app.
@app.route('/')
def index():
    ''' Add comment here '''
    booths = session.query(Booths).order_by(asc(Booths.name))
    items = session.query(Items).order_by(Items.id.desc()).limit(10)
    return render_template('index.html', booths=booths, items=items)


# List of all items
@app.route('/items/')
def allItems(booth_id=None):
    ''' Add comment here '''
    items = session.query(Items).order_by(asc(Items.name))
    return render_template('items.html', items=items)


# Contact page
@app.route('/about/')
def about():
    return render_template('about.html')

# This section contains the routes and functions to manage booths

# Add a booth
@app.route('/booth/new/', methods = ['GET', 'POST'])
def addBooth():
    ''' Add comment here '''
    if request.method == 'POST':
        newBooth = Booths(name=request.form['name'],
                          email=request.form['email'],
                          phone=request.form['phone'],
                          image=request.form['image'])
        session.add(newBooth)
        session.commit()
        flash('New booth for %s successfully created!' % newBooth.name)
        return redirect(url_for('index'))
    else:
        return render_template('addbooth.html')


# Edit booth
@app.route('/booth/<int:booth_id>/edit/', methods=['GET', 'POST'])
def editBooth(booth_id=None):
    ''' Add comment here. '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    if request.method == 'POST':
        if request.form['name']:
            booth.name = request.form['name']
        if request.form['email']:
            booth.email = request.form['email']
        if request.form['phone']:
            booth.phone = request.form['phone']
        if request.form['image']:
            booth.image = request.form['image']
        session.add(booth)
        session.commit()
        flash('Booth information for %s successfully edited' % booth.name)
        return redirect(url_for('index'))
    else:
        return render_template('editBooth.html', booth=booth)


# Delete booth
@app.route('/booth/<int:booth_id>/delete/', methods=['GET', 'POST'])
def deleteBooth(booth_id=None):
    ''' Add comment here. '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    if request.method == 'POST':
        if request.form['name'] == booth.name:
            session.delete(booth)
            session.commit()
            flash('%s successfully deleted!' % booth.name)
            return redirect(url_for('index'))
        else:
            flash('Name did not match.  Try again or cancel.')
            return render_template('deleteBooth.html', booth=booth)
    return render_template('deleteBooth.html', booth=booth)


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
def item(booth_id=None, item_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id).one()
    return render_template('item.html', booth=booth, item=item)


# Add item
@app.route('/booth/<int:booth_id>/new/', methods=['GET', 'POST'])
def addItem(booth_id=None):
    ''' This function is used to create new items for a booth.'''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    if request.method == 'POST':
        item = Items(name=request.form['name'],
                     description=request.form['description'],
                     price=request.form['price'],
                     category=request.form['category'],
                     booth_id=booth.id,
                     image=request.form['image'])
        session.add(item)
        session.commit()
        flash('Items successfully add to %s!' % booth.name)
        return redirect(url_for('booth', booth_id=booth.id))
    else:
        return render_template('addItem.html', booth=booth)


# Edit item
@app.route('/booth/<int:booth_id>/<int:item_id>/edit/', methods = ['GET', 'POST'])
def editItem(booth_id=None, item_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['price']:
            item.price = request.form['price']
        if request.form['category']:
            item.category = request.form['category']
        if request.form['image']:
            item.image=request.form['image']
        session.add(item)
        session.commit()
        flash('%s successfully updated!' % item.name)
        return redirect(url_for('booth', booth_id=booth.id))
    else:
        return render_template('editItem.html', item=item, booth=booth)


# Delete item
@app.route('/booth/<int:booth_id>/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(booth_id=None, item_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name'] == item.name:
            session.delete(item)
            session.commit()
            flash('%s successfully deleted!' % item.name)
            return redirect(url_for('booth', booth_id=booth.id))
        else:
            flash('Name did not match. Try again or cancel.')
            return redirect(url_for('deleteItem', booth_id=booth.id, item_id=item.id))
    else:
        return render_template('deleteItem.html', booth=booth, item=item)


################################## JSON API ####################################

# All Items Info
@app.route('/items/json')
def allItemsJOSN(booth_id=None):
    ''' Add comment here '''
    items = session.query(Items).order_by(asc(Items.name)).all()
    return jsonify(items=[i.serialize for i in items])

# Booth Info
@app.route('/booth/<int:booth_id>/json')
def boothJSON(booth_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    items = session.query(Items).filter_by(booth_id=booth_id)
    return jsonify(items=[i.serialize for i in items])


# Item Info
@app.route('/booth/<int:booth_id>/<int:item_id>/json')
def itemJSON(booth_id=None, item_id=None):
    ''' Add comment here '''
    booth = session.query(Booths).filter_by(id=booth_id).one()
    item = session.query(Items).filter_by(id=item_id).one()
    return jsonify(item=item.serialize)


############################### Login Functions ################################

@app.route('/login/')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return render_template('login.html')
    return render_template('login.html')

################################################################################

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug='True', host='0.0.0.0', port=8000)

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
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
# APPLICATION_NAME = "Flea Market App"



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
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


################################### Log Out ####################################

@app.route('/gdisconnect')
def gdisconnect():
    access_token = credentials.access_token
    print access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    print url
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        name = login_session['username']
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']

        response = make_response(
            json.dumps('Successfully disconnected (gmail).'), 200)
        response.headers['Content-Type'] = 'application/json'
        print "user %s successfully disconnected!" % name
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user (gmail).', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


################################################################################

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug='True', host='0.0.0.0', port=8000)

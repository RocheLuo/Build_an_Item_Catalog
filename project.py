from flask import Flask, render_template, redirect, url_for, jsonify, request, flash,make_response
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets,FlowExchangeError
import random, string,httplib2,json,requests

app = Flask(__name__)


from database_setup import Base, Item, Shop
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///item.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Buid an Item Catalog"

# Making the login function

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in list(range(32)))
    login_session['state'] = state
    return render_template("login.html",STATE=state)

# Making an API Endpoint ()

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
        return response

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
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
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
    print("done!")
    return output



@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print ('In gdisconnect access token is %s'), access_token
    print ('User name is: ')
    print (login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/catalog/JSON')
def catalog_JSON():
    shops = session.query(Shop).all()
    ## TO DO items NO.
    print("yes")
    return jsonify(Shop=[i.serialize for i in shops])


# Making the main catalog

@app.route('/')
def all_list():
    items = session.query(Item).all()
    shops = session.query(Shop).all()
    print("yes")
    return render_template('main.html', items=items, shops=shops)


# Making the shop-catalog

@app.route('/shop/<string:shop_name>')
def shop_items(shop_name):
    shops = session.query(Shop).all()
    shop = session.query(Shop).filter_by(name=shop_name).one()
    items = session.query(Item).filter_by(shop_id=shop.id).all()
    N = len(items)
    return render_template('shop_item.html', items=items, shops=shops, shop_name=shop_name, N=N)


# Making the item information

@app.route('/shop/<string:shop_name>/<int:item_id>')
def item_info(item_id,shop_name):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item_info.html',item=item)


# Add new item in the shop

@app.route("/item/add", methods=["GET", "POST"])
def add_item():
    # if "username" not in login_session:
    #     return redirect("/login")
    if request.method == "POST":
        newItem = Item(title=request.form['title'],price='$'+request.form['price'],shop=request.form['shop'])
        session.add(newItem)
        session.commit()
        flash("A new item has been created!")
        return redirect(url_for('all_list'))
    else:
        shops = session.query(Shop).all()
        return render_template('add.html',shops=shops)

#
# Edit item inforamtion in the shop

@app.route('/shop/<string:shop_name>/<int:item_id>/edit',methods=['GET', 'POST'])
def edit_item(item_id,shop_name):
    if "username" not in login_session:
        return redirect("/login")
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == "POST":
        item.title=request.form["title"]
        session.add(item)
        session.commit()
        flash("The item has been edited!")
        return redirect(url_for("shop_items",shop_name=shop_name))
    else:
        return render_template("edit.html",item=item,shop_name=shop_name)

# Delete item in the shop

@app.route("/shop/<string:shop_name>/<int:item_id>/delete",methods=['GET', 'POST'])

def delete_item(item_id,shop_name):
    if "username" not in login_session:
        return redirect("/login")
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == "POST":
        session.delete(item)
        session.commit()
        flash("The item has been deleted!")
        return redirect(url_for("shop_items", shop_name=shop_name))
    else:
        return render_template("delete.html",item=item,shop_name=shop_name)
    # return render_template('delete.html')



if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
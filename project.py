from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()


#API Endpoints (GET request)
@app.route('/restaurants/<int:restaurant_id>/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def restaurantMenuItemJson(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)


@app.route('/')
@app.route('/restaurants/')
def restaurants():
    # Shows all restaurants


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['POST', 'GET'])
def newRestaurant():
    # Adds a new restaurant to the database.


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['POST', 'GET'])
def editRestaurant(restaurant_id):
    # Edits an existing restaurant in the database.


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['POST', 'GET'])
def deleteRestaurant(restaurant_id):
    # Deletes an existing restaurant in the database.


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['POST', 'GET'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)
    

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['POST', 'GET'])
def editMenuItem(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        menuItem.name = request.form['name']
        menuItem.description = request.form['description']
        menuItem.price = request.form['price']
        menuItem.course = request.form['course']
        session.add(menuItem)
        session.commit()
        flash("Menu item edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, menuItem=menuItem)
        

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['POST', 'GET'])
def deleteMenuItem(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(menuItem)
        session.commit()
        flash("Menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, menuItem=menuItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

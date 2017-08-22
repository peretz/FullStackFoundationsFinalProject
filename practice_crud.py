from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
dbsession = sessionmaker(bind = engine)
session = dbsession()

# CREATE restaurant and menuitem objects for database

# myfirstrestaurant = restaurant(name = "pizza palace")
# session.add(myfirstrestaurant)
# session.commit()
# 
# cheesepizza = menuitem(name="cheese pizza", description = "made with all natural ingredients and fresh mozzarella", course="entree", price="$8.99", restaurant=myfirstrestaurant)
# session.add(cheesepizza)
# session.commit()

# READ restaurant and menuitem 

# firstresult = session.query(restaurant).first()
# print (firstresult.name)
# 
# items = session.query(menuitem).all()
# for item in items:
#         print item.name
# 

# UPDATE menuitem

def printMenuItem(itemName):
    menuItems = session.query(MenuItem).filter_by(name= itemName)
    for items in menuItems:
        print items.id
        print items.price
        print items.restaurant.name
        print "\n"

# printMenuItem('Veggie Burger')
# 
# UrbanVeggieBurger = session.query(MenuItem).filter_by(id=9).one()
# UrbanVeggieBurger.price = '$2.99'
# session.add(UrbanVeggieBurger)
# session.commit() 
# 
# printMenuItem('Veggie Burger')

# DELETE menuitem

printMenuItem('Spinach Ice Cream')

spinach = session.query(MenuItem).filter_by(name= 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 

printMenuItem('Spinach Ice Cream')

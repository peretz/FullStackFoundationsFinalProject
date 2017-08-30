# Full Stack Foundations: Final Project - Restaurant and menu management system.

This project is based on Udacity's Full Stack Foundations final project. The objective
of this project is learning the key concepts around implementing a full stack web implementation,
which includes:

* *CRUD operations*: Create, Read, Update and Delete.
* *Pros and Cons* of using ORMs (e.g. SQLalchemny)
* *IP, TCP and HTTP protocols.*
* Implementation of POST and GET requests using python's *HTTPBaseServer library*.
* Implementation of POST and GET requests using a *python framework* (e.g. FLASK)
* Flask's routing, templates, forms, redirects, message flashing, styling and JSONify.

In order to learn these concepts, the project implements a Restaurants and Menu management system.

## File Structure.

There are four files:

* *database_setup.py:* Defines the database objects using SQLAlchemy as ORM.
* *lotsofmenus.py:* Contains restaurants and menus to create in the database.
* *webserver.py:* Contains the HTTPBaseServer implementation.
* *project.py:* Contains Flask's implementation.

## Run HTTPBaseServer implementation.

1. Access the vagrant environment
2. Run database_setup.py to create the database
3. Run lotsofmenus.py to populate the database
4. Run webserver.py and navigate to localhost:5000 in your browser

## Run the implementation that uses Flask.

1. Access the vagrant environment
2. Run database_setup.py to create the database
3. Run lotsofmenus.py to populate the database
4. Run project.py and navigate to localhost:5000 in your browser

If you ran successfully the previous steps, you should be able to:
* See a complete list of all restaurants.
* Create, edit and delete a restaurant.
* Access the menu for a specific restaurant.
* Create, edit and delete items in the menu.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
dbsession = sessionmaker(bind = engine)
session = dbsession()


class webServerHandler(BaseHTTPRequestHandler):

    def __printAllRestaurants(self):
        output = ""
        output += "<html><body>"
        
        restaurants = session.query(Restaurant).all()
        for restaurant in restaurants:
            output += "<p>" + restaurant.name + "<br>"
            output += "<a href=restaurant/" + str(restaurant.id) + "/edit>Edit</a><br>"
            output += "<a href=restaurant/" + str(restaurant.id) + "/delete>Delete</a><br>"
            output += "<br></p>"

        output += "<p><a href=/restaurants/new>Make a New Restaurant Here.</a></p>"
        output += "</body></html>"
        self.wfile.write(output)

        
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.__printAllRestaurants()
                return


            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
                output += "<input name='newRestaurantName' type='text' placeholder = 'New Restaurant Name'>"
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                print output
                return


            if self.path.endswith("/edit"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Recover restaurant ID from URL
                restaurantID = self.path.split("restaurant/")[1].split("/edit")[0]
                restaurant = session.query(Restaurant).filter_by(id= restaurantID).one()
                output = ""
                output += "<html><body>"
                output += "<h1>" + restaurant.name + "</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/edit'>" % restaurantID
                output += "<input name='newRestaurantName' type='text' placeholder = 'New Restaurant Name'>"
                output += "<input type='submit' value='Rename'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                print output
                return


            if self.path.endswith("/delete"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Recover restaurant ID from URL
                restaurantID = int(self.path.split("restaurant/")[1].split("/delete")[0])
                restaurant = session.query(Restaurant).filter_by(id= restaurantID).one()
                output = ""
                output += "<html><body>"
                output += "<h1> Are you sure you want to delete " + restaurant.name + "</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete'>" % restaurantID
                output += "<input type='submit' value='Delete'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    newRestaurantName = fields.get('newRestaurantName')
                    newRestaurant = Restaurant(name = newRestaurantName[0])
                    session.add(newRestaurant)
                    session.commit()

            elif self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    newRestaurantName = fields.get('newRestaurantName')
                    restaurantID = self.path.split("restaurant/")[1].split("/edit")[0]
                    restaurant = session.query(Restaurant).filter_by(id= restaurantID).one()
                    restaurant.name = newRestaurantName[0]
                    session.add(restaurant)
                    session.commit()

            elif self.path.endswith("/delete"):
                restaurantID = self.path.split("restaurant/")[1].split("/delete")[0]
                restaurant = session.query(Restaurant).filter_by(id= restaurantID).one()
                session.delete(restaurant)
                session.commit()

            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/restaurants')
            self.end_headers()

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()


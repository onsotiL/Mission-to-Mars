#use Flask and Mongo to begin creating Robin's web app
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#set up Flask:
app = Flask(__name__)

# tell Python how to connect to Mongo using PyMongo.
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#set up our Flask routes(Flask routes bind URLs to functions)
#one for the main HTML page everyone will view when visiting the web app
#one to scrape new data using the code we've written.
# EG:  URL "ourpage.com/" brings us to  homepage of our web app.
# URL "ourpage.com/scrape" will activate the scraping code.

#define the route for the HTML
#This function  links our visual representation of our work, our web app, to the code that powers it.
@app.route("/") # tells Flask what to display when looking at the home page,
def index():
    #within this 1. use pymomgo to find mars collection in database & assign path to mars varaible
               # 2. return an HTML template using an index.html file.
               # mars=mars) tells Python to use the "mars" collection in MongoDB.
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars) 


#set up our scraping route
#this  route will be the "button" of the web application
#it will scrape updated data when we tell it to from the homepage of our web app
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

#Now that we've gathered new data, we need to update the database using .update().
mars.update({}, mars_data, upsert=True)


if __name__ == "__main__":
   app.run()






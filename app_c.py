from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars_c

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Use flask_pymongo to set up mongo connection
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index_c.html", mars=mars)
    
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars_c.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful!"

if __name__ == "__main__":
    app.run()
   
         
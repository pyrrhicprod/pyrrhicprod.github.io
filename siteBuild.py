from flask import Flask, request, render_template, g, Markup
import sqlite3
import datetime
import markdown
from flask_frozen import Freezer
import os
import shutil

app = Flask(__name__)
freezer = Freezer(app)

#Date
today = datetime.datetime.today()

#variables
logo = 'newPyrrhicLogo.png'


app.database = "Pyrrhic_DB"
def connectdb():
    # type: () -> object
    return sqlite3.connect(app.database)

def movehome():
    files = os.listdir('build')
    for file in files:
        shutil.move('build/' + file, file)
    
conn = connectdb()

#Pages needed
    #Home Page
        #Home page has all teams, scores and rankings
    #School pages
        #One per school

@app.route("/")
def homepage():
    plogo = logo
    homeWork = conn.execute("SELECT * from home_work").fetchall()
    return render_template('index.html', **locals())

@app.route("/about.html")
def about():
    plogo = logo
    staffInfo = conn.execute("SELECT * from about_staff").fetchall()
    return render_template('about.html', **locals())

@app.route("/contact.html")
def contact():
    plogo = logo
    staffInfo = conn.execute("SELECT * from about_staff").fetchall()
    return render_template('contact.html', **locals())

if __name__ == "__main__":
    """ Builds this site.
        """
    print("Building website...")
    app.debug = False
    app.testing = True
    freezer.freeze()
    movehome()
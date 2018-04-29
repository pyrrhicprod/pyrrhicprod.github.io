from flask import Flask, request, render_template, g, Markup
import sqlite3
import datetime
import markdown
from flask_frozen import Freezer
import os
import shutil
from youtubeAPI import Video

app = Flask(__name__)
freezer = Freezer(app)

#Date
today = datetime.datetime.today()

#variables
logo = 'pyrrhic_logo.jpg'



app.database = "Pyrrhic_DB"
def connectdb():
    # type: () -> object
    return sqlite3.connect(app.database)

def movehome():
    files = os.listdir('build')
    for file in files:
        shutil.move('build/' + file, file)


def get_markdown(md):
    path = 'markdown/'+md
    f = open(path, 'r')
    content = markdown.markdown(f.read())
    output = Markup(markdown.markdown(content))
    return output
    
conn = connectdb()

#Pages needed
    #Home Page
        #Home page has all teams, scores and rankings
    #School pages
        #One per school

@app.route("/")
def homepage():
    plogo = logo
    title = 'Video Production | Jersey City | Pyrrhic Productions'
    homeWork = conn.execute("SELECT * from home_work").fetchall()
    description = get_markdown('index.md')
    return render_template('index.html', **locals())

@app.route("/about.html")
def about():
    plogo = logo
    title = 'About | Jersey City | Pyrrhic Productions'
    staffInfo = conn.execute("SELECT * from about_staff").fetchall()
    description = get_markdown('about.md')
    return render_template('about.html', **locals())

@app.route("/contact.html")
def contact():
    plogo = logo
    title = 'Contact | Jersey City | Pyrrhic Productions'
    staffInfo = conn.execute("SELECT * from about_staff").fetchall()
    description = get_markdown('contact.md')
    return render_template('contact.html', **locals())

@app.route("/<work>.html")
def work(work):
    plogo = logo
    content = conn.execute("SELECT * from home_work where urlName = '{}'".format(work)).fetchall()[0]
    description = get_markdown('index.md')
    ytID = content[4].split('=')[1]
    ytVid = Video(ytID)
    print(ytVid.views)
    title =  content[1] + ' | Jersey City | Pyrrhic Productions'
    return render_template('content.html',**locals())


@freezer.register_generator
def work():
    homeWork = conn.execute("SELECT * from home_work").fetchall()
    for i in homeWork:
        work = i[7]
        yield {'work':work}

if __name__ == "__main__":
    """ Builds this site.
        """
    print("Building website...")
    app.debug = False
    app.testing = True
    freezer.freeze()
    movehome()

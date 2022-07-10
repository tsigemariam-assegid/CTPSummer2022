from flask import Flask, render_template, redirect, url_for

import json


beginner_contents = { 
    "0" : {
    'id' : "0",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "1" : {
    'id' : "1",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "2" : {
    'id' : "2",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "3" : {
    'id' : "3",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "4" : {
    'id' : "4",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    }

}

intermediate_contents = { 
    "0" : {
    'id' : "0",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "1" : {
    'id' : "1",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "2" : {
    'id' : "2",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "3" : {
    'id' : "3",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    },
    "4" : {
    'id' : "4",
    'videoURL' : [],
    'homeworkURL' : [],
    'hwSub' : [],
    }

}

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/beginner/<week>')
def view_beginner(week):
    global beginner_contents
    beginner = beginner_contents[week]
    return render_template("beginner.html", beginner = beginner)

@app.route('/intermediate/<week>')
def view_intermidate(week):
    global intermediate_contents
    intermediate = intermediate_contents[week]
    return render_template("intermediate.html", intermediate = intermediate)



if __name__ == '__main__':
   app.run(debug = True)



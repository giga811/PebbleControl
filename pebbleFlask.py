# coding=utf8
"""
# Code name: pebbleFlask

# pebbleFlask program

"""
# flask imports
from flask import Flask
import os

# configuration
DEBUG = True
SECRET_KEY = 'pebbly'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def keyCode(keycode):
    cmd = """
    osascript -e 'tell application "System Events"
    key code """ + keycode + """
    end tell'
    """
    os.system(cmd)

@app.route('/slideshow')
def slideshow():
    cmd = """
    osascript -e '
    tell application "Microsoft PowerPoint"
    delay 1
    set slideShowSettings to slide show settings of active presentation
    run slide show slideShowSettings
    end tell'
    """
    os.system(cmd)
    print "Go slideshow"
    return "ok"

@app.route('/right')
def goright():
    keyCode("124")
    print "Go right"
    return "ok"

@app.route('/left')
def goleft():
    keyCode("123")
    print "Go left"
    return "ok"

@app.route('/')
def index():
    return "pebbleFlask server running."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

# coding=utf8
"""
# Code name: pebbleFlask

# pebbleFlask program

"""
# flask imports
from flask import Flask, render_template
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

def alphabetStroke(c):
    cmd = """
    osascript -e 'tell application "System Events"
    keystroke \"""" + c[0] + """\"
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

@app.route('/keycode/<int:x>')
def keycode_controller(x):
    # this keycode_controller has some security risk
    if x > 128 or x < 0:
        return "invalid keycode"
    else:
        keyCode(str(x))
        print "Keycode ", x
        return "ok"

@app.route('/keychar/<string:c>')
def keychar_controller(c):
    if len(c) > 1:
        return "invalid keychar"
    else:
        alphabetStroke(c)
        print "Keychar ", c
        return "ok"

@app.route('/control.html')
def controlhtml():
    return render_template('control.html')


@app.route('/')
def index():
    return "pebbleFlask server running."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

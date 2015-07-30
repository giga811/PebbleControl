# PebbleControl

## Description
PebbleControl is flask api app for controlling your mac pc.
For example it can control your presentation using your smartphones, smartwatches, wearable devices.

## How to run
```sh
$ pip install flask
$ python pebbleFlask.py
```

## Functions

* /right - go right. keystroke for rightarrow (→)
* /left - go left. keystroke for leftarrow (←)
* /slideshow - Activate presentation mode for current Powerpoint slide
* /keycode/<int:x\> - keycode for x
* /keychar/<string:c\> - keystroke for c (one character)
* /control.html - mobile, web gui for basic control

## Example keycode
123 - rightarrow
124 - leftarrow
125 - downarrow
126 - uparrow

other keycode list http://apple.stackexchange.com/questions/36943/how-do-i-automate-a-key-press-in-applescript

#!/usr/bin/python3
"""script that starts flask web application"""

from flask import  Flask
app = Flask(__name__)

@app.route('/',strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB!"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun():
    """display "c",followed by the value of the text variable"""
    return 'c' + text.replace('_', '')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display "python",followed by the value of the text variable"""
    return 'python ' + text.replace('_', '')

if __name__ == ' __main__'
app.run(host='0.0.0.0', port ='5000')

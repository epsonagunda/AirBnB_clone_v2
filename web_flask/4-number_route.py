#!/usr/bin/python3
"""
script that starts flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def index():
    """return Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """return HBNB"""
    return 'HBNB'

@app.route('/c/<text>')
def cisfun():
    """display "c", followed by the value of the text varriable"""
    return 'c' + text.replace('_', '')

@app.route('/python')
@app.route('/python/<text>')
def pythoniscool(text='is cool'):
    """ display "python", followed by the value of the text varriable"""
    return 'python ' + text.replce('_','')

@app.route('/number/<int:n>')
def imanumber(n):
    """display "n is a nmber" only if n is an integer"""
    return "{:d} is a number ".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


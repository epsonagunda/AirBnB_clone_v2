#!/usr/bin/python3
"""
script that starts a flask web application with 7 function
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
    """Return HBNB"""
    return 'HBNB'

@app.route('/c/<text>')
def cisfun():
    """display 'C', follwed by the value of the text varriable"""
    return 'C' + text.replace('_', ' ')

@app.route('/python')
@app.route('/python/<text>')
def pythoniscool(text= 'is cool'):
    """dislay 'python', followed by the value of the text variable'"""
    return 'python ' + txt.replace('_', ' ')

@app.route('/number/<int:n>')
def imanumber(n):
    """display 'n is a number' only if n is an interger"""
    return "{:d} is a number".format(n)
@app.route('/number_template/<int:n>')
def numberandtemplates(n):
    """display a html page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

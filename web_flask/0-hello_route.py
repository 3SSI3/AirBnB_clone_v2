#!/usr/bin/python3
"""
starts a Flask web application
Web app listens on 0.0.0.0 port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

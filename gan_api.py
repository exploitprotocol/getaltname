"""GetAltName Web API."""
from modules import get_san
from modules import json_format
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return index page."""
    return "<center><h1>It works!</h1></center>"


@app.route('/<string:host>')
def return_san(host):
    """Return a JSON string with SANS's found."""
    try:
        sans = get_san(host, 443)
    except Exception as e:
        return jsonify({'err': 'Unable to connect.'})
    json_sans = {'count': len(sans), 'domains': list(sans)}
    return jsonify(json_sans)


if __name__ == '__main__':
    app.run()
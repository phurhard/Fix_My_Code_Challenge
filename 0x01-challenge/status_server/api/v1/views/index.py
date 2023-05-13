#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views

from api.v1.app import *


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})i

if __name__ == '__main__':
    app.run()

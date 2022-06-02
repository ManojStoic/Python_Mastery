"""
Web server - Stores and loads all static pages related to a website

http.server -> python lib to implement http servers(web servers)

Flask -> Python sync framework (analogy - micro-kitchen)
Django -> Python sync framework (analogy - macro-kitchen)

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
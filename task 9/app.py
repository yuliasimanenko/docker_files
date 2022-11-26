from flask import Flask
from flask import request
import os
import socket
import db

app = Flask(__name__)


@app.route('/')
def index():
    return db.get_stats()


@app.route('/stat')
def stat():
    client_info = request.headers.get('User-Agent')
    return db.increment_and_get_stats(client_info)


@app.route("/about")
def about():
    html = "<h3>Hello, Julia Simanenko</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
from flask import Flask
import os
import socket

app = Flask(__name__)

counter = 0

@app.route('/')
def index():
    global counter
    return f'{counter}'


@app.route('/stat')
def stat():
    global counter
    counter += 1
    return f'{counter}'


@app.route("/about")
def about():
    html = "<h3>Hello, Julia Simanenko</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
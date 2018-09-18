#!/usr/bin/env python
from colorhash import ColorHash
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    msg = f"""
    <html>
    <head>
        <style>
            body {{
                background: {ColorHash(hostname).hex};
            }}

            h1, p {{
                background: #fff;
                color: #000;
            }}
        </style>
    </head>
    <body>
        <h1>Hello from {hostname}!</h1>
    </body>
    </html>
    """

    return msg


if __name__ == "__main__":
    app.run(host='0.0.0.0')

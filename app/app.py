"""
Demo for flask appliation in docker.
"""
import os
import socket
import random
from flask import Flask
from flask import render_template


app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(
    ["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def main():
    """Main function."""
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    """Get Color function."""
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    """Read file name function."""
    #file_test = open("/data/testfile.txt", encoding='utf-8')
    with open("/data/testfile.txt", encoding='utf-8') as file_test:
        contents = file_test.read()
    return render_template('hello.html',
    name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

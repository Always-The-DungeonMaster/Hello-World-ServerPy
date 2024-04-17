# This file should be named server.py
# This is a bare-bones template from week 2 of App Development using Microservices and Serverless
from flask import Flask

app = Flask("My Hello World Application")

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run(debug=True)
# When no port is specified, starts at default port 5000

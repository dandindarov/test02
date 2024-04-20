from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_dan():
    return "Hello Dan"

app.run()




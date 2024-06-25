# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)} , my name is Remon !'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80

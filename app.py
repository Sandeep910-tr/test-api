from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/posts")
def posts():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/posts").json())

@app.route("/comments")
def comments():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/comments").json())
     "status": "successfully triggered auto deployment"

@app.route("/albums")
def albums():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/albums").json())

if __name__ == "__main__":
    app.run(debug=True)

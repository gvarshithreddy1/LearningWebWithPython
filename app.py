from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

FRIENDS= [
  {
    "name":"Arun",
    "dank": "yes",
    "good": "yes"
  },
  {
    "name":"Chetan",
    "dank": "yes",
    "good": "yes"
  },
  {
    "name":"Madhu",
    "dank": "yes",
    "good": "yes"
  },
  {
    "name":"Venu",
    "dank": "yes",
    "good": "yes"
  },
  {
    "name":"Abhi",
    "dank": "yes",
    "good": "yes"
  }
  
]
  
  


@app.route("/")
def hello_world():
    return render_template('home.html',
                          friends = FRIENDS)
@app.route("/api/friends")
def json():
  return jsonify(FRIENDS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
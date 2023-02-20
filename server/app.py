from flask import Flask, render_template
from firebase import firebase
import json
 
app = Flask(__name__, template_folder='../')
fb_app = firebase.FirebaseApplication('https://lingulink-default-rtdb.firebaseio.com/', None)
result = fb_app.get('/', None)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route('/levelpick/<int:data>')
def levelpick(data):
    result = fb_app.get('/', None)
    return result["Questions"][data]




app.run(port=5000, debug=True)
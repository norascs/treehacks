from flask import Flask
from firebase import firebase
import json
 
app = Flask(__name__)
fb_app = firebase.FirebaseApplication('https://lingulink-default-rtdb.firebaseio.com/', None)
result = fb_app.get('/', None)
print(result["Questions"][0])
@app.route('/levelpick/int:<data>')
def levelpick(data):
    result = fb_app.get('/', None)
    return result["Questions"][data]




#app.run(port=5000, debug=True)
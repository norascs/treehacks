from flask import Flask
 
app = Flask(__name__)
database = {}

@app.route('/flask', methods=['GET'])
def index():
    return 'he he he haw'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
from datetime import datetime
from flask import make_response, Response
from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
@app.route('/health')
def health():
    return "Health is up"

@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    strLine = request.json['Item']
    return Response(json.dumps(strLine), mimetype='application/json')

if __name__ == "__main__":
    app.run()
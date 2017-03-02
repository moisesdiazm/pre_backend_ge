"""Cloud Foundry test"""
import json, time, random
from flask import Flask, make_response
from flask_cors import CORS, cross_origin

import os

app = Flask(__name__)
CORS(app)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)

@app.route('/liveplot-data')
def liveplot_data():
    # Create a PHP array and echo it as JSON
    data = [time.time() * 1000, random.random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/overview-data')
def overview_data():
    # Create a PHP array and echo it as JSON
    data = {
        'cpuLoad': random.random() * 100,
        'networkSent': random.random() * 500,
        'networkRecieve': random.random() * 100,
        'millionSavings': random.random(),
        'healthStatus': random.random() * 100
    }
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/health-data')
def health_data():
    # Create a PHP array and echo it as JSON
    data = {
        'hpcEff': random.random(),
        'hpcWr': random.random(),
        'hptEff': random.random(),
        'lptEff': random.random(),
        'lptWr': random.random()
    }
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/economic-data')
def economic_data():
    # Create a PHP array and echo it as JSON
    data = {
        'totalCost': random.random()*10000,
        'totalSavings': random.random()*10000,
        'totalProfit': random.random()*10000,
        'goalCompletions': random.random()*100
    }
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/critical-data')
def critical_data():
    # Create a PHP array and echo it as JSON
    data = {
        'mwPower': random.random()*20,
        'fuelFlow': random.random()*50000,
        'ambPs': random.random()*20,
        'ambTmp': random.random()*60
    }
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/events-data')
def events_data():
    # Create a PHP array and echo it as JSON
    data = [
        {
            'eid': 'OR9842',
            'date': '2020-08-09T11:24:20',
            'detail': 'Engine provides expected output in average',
            'status': 'Running',
            'label': 'label-success'
        },
        {
            'eid': 'OR9843',
            'date': '2020-08-09T11:24:20',
            'detail': 'Engine MW is below lower limit',
            'status': 'Warning',
            'label': 'label-warning'
        },
        {
            'eid': 'OR9844',
            'date': '2020-08-09T11:24:20',
            'detail': 'Engine provides erratic output',
            'status': 'Danger',
            'label': 'label-danger'
        }
    ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
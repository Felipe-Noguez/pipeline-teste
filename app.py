import os

import elasticapm
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.metrics.base_metrics import MetricSet

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Édiplo!'

@app.route('/teste')
def teste_hello_world():
    return 'Teste Hello, World!'

@app.route('/error')
def error():
    raise Exception('This is a test error!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

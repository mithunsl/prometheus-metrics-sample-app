from flask import Flask, Response, request
import prometheus_client
from prometheus_client import Counter
graphs = {}
graphs['c'] = Counter('python_request_operations_total', "The total number of requests processed")

_INF = float("inf")
app = Flask(__name__)

@app.route("/")
def hello():
    graphs['c'].inc()
    return 'Hello World'

@app.route("/metrics")
def metrics():
    res = []
    res.append(prometheus_client.generate_latest(graphs['c']))

    return Response(res, mimetype="text/plain")


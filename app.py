from datetime import datetime
import os
import random
import time

from flask import Flask
import requests


app = Flask(__name__)
EXAMPLE_SERVICE = os.environ["EXAMPLE_SERVICE"]


@app.route('/')
def root():
    start = datetime.now()

    num_requests = random.randint(0, 50)
    responses = []
    for _ in range(0, num_requests):
        responses.append(requests.get(f"{EXAMPLE_SERVICE}/random/number").json())

    finish = datetime.now()
    duration = finish - start 

    return {
        "location": "/",
        "num_requests": num_requests,
        "responses": responses,
        "time": float(duration.total_seconds()),
    }


@app.route("/random/number")
def random_number():
    # Simulate some problem in the app logic by sleeping for random time
    # This is a new API endpoint that we will rewrite in Golang later
    time.sleep(random.randint(0.0, 1.0))
    return {
        "location": "/random/number",
        "number": random.randint(0, 9999)
    }


@app.route('/healthz')
def health():
    return {
        "healthy": True
    }

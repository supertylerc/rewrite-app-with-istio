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
        responses.append(random_number())

    finish = datetime.now()
    duration = finish - start 

    return {
        "location": "/",
        "num_requests": num_requests,
        "responses": responses,
        "time": float(duration.total_seconds()),
    }


def random_number():
    # Simulate some problem in the app logic by sleeping for random time
    # This will later become a new API endpoint that we break out
    time.sleep(random.randint(0.0, 1.0))
    return {
        "number": random.randint(0, 9999)
    }


@app.route('/healthz')
def health():
    return {
        "healthy": True
    }

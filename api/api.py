"""This API methods file."""

import json
import sys
from bottle import run, get, response
from collections import defaultdict


sys.path.append("..")

from core.app import Tweet


@get('/most_relevants/<user>')
def api_relevants(user):
    app = Tweet()
    response.content_type = 'application/json'
    tweets = []
    status = 200

    try:
        tweets = app.get_tweets(user)
    except Exception as e:
        print e
        status = 400
        raise

    response.status = status
    return json.dumps(tweets)

@get('/most_mentions/<user>')
def api_mentions(user):
    app = Tweet()
    response.content_type = 'application/json'
    tweets = []
    status = 200

    try:
        tweets = app.get_tweets(user)
    except Exception as e:
        print e
        status = 400
        raise

    response.status = status
    return json.dumps(tweets)


run(host='localhost', port=8000, debug=True)

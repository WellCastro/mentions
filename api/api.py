"""This API methods file."""

import json
import sys
import bottle
from bottle import run, get, response
import logging

sys.path.append("..")

from core.app import Tweet

# config logs
logging.basicConfig(filename='../logs/api.log', level=logging.INFO)

@get('/most_relevants/<user>')
def api_relevants(user):
    app = Tweet()
    response.content_type = 'application/json'
    tweets = []
    status = 200
    try:
        tweets = app.get_tweets(user)
        filter_tweets = app.filters_tweets(tweets, int(user))
        tweets = app.result_final(filter_tweets)
        logging.info('Get user: {0}'.format(user))
    except Exception as e:
        logging.error('User: {0}/{1}'.format(user, e))
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
        tweets = app.filters_tweets(tweets, int(user))
        tweets = app.group_tweets(tweets, int(user))
        logging.info('Get user: {0}'.format(user))
    except Exception as e:
        logging.error('User: {0}/{1}'.format(user, e))
        status = 400
        raise

    response.status = status
    return json.dumps(tweets)

if __name__ == "__main__":
    run(host='localhost', port=8001)

app = bottle.default_app()

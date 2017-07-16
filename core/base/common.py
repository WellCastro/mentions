"""Class base project."""
import os
import json


class Base(object):

    def __init__(self):
        self.url_tweets = "http://tweeps.locaweb.com.br/tweeps"
        self.headers_tweets = {"Username": "wcesarc@gmail.com"}
        self.twitter_url = "https://twitter.com/"
        self.tweet_url = "https://twitter.com/i/moments/"
        self.base_dir = os.getcwd()
        self.user_test = 42
        self.url_most_mentions = "http://198.199.65.250:8001/most_mentions/"
        self.url_relevants = "http://198.199.65.250:8001/most_relevants/"

    def get_file_tweets(self, name):
        path = "{0}/valueobject/{1}".format(self.base_dir, name)
        json_data = None
        try:
            with open(path, "r") as data:
                json_data = json.load(data)
        except Exception, e:
            print e
            pass

        return json_data
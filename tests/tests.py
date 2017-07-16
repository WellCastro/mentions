import requests
import sys
import json
sys.path.append("..")

from core.base.common import Base
from core.app import Tweet

class TestClass:

    base = Base()
    core = Tweet()
    user_test = base.user_test

    def mock_tweets(self):
        # mock data tweets json
        tweets = self.base.get_file_tweets('tweets.json')

        return tweets

    def test_order_relevants(self):
        """GET tweets from order relevants."""
        list_followers = []
        tweets = self.mock_tweets()

        # test functions core app
        filter_tweets = self.core.filters_tweets(tweets, int(self.user_test))
        # format to result final
        tweets = self.core.result_final(filter_tweets)
        # get order followers by count and assert list
        for t in tweets:
            count = t.get('user').get('followers')
            list_followers.append(count)

        assert list_followers == [707, 662, 272, 146]

    def test_group_mentions(self):
        """GET tweets from group users."""
        list_users = []
        list_users_test = ['collins_clovis_dr', 'macgyver_iv_hubert', 'tracy_connelly', 'conn_trenton']
        tweets = self.mock_tweets()

        # test functions core app filter tweets
        filter_tweets = self.core.filters_tweets(tweets, int(self.user_test))
        # group function
        grouped = self.core.group_tweets(filter_tweets, int(self.user_test))
        print json.dumps(grouped)
        for user in grouped:
            list_users.append(user)

        assert list_users == list_users_test

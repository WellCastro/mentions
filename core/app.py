"""Core from tweets mentions."""
import requests
from base.common import Base


class Tweet(Base):

    def __init__(self, *args, **kwargs):
        super(Tweet, self).__init__(*args, **kwargs)

    def id_mention(self, obj=None):
        try:
            return int(obj.get('user_mentions')[0].get('id'))
        except IndexError:
            return None

    def get_tweets(self, user):
        url = self.url_tweets
        header = self.headers_tweets
        result = None
        try:
            r = requests.get(url, headers=header)
            filter_tweets = self.filters_tweets(r.json(), int(user))
            result = self.result_final(filter_tweets)
        except Exception as e:
            # log
            print e
            raise

        return result

    def filters_tweets(self, data=None, user=None):
        result_filter = []
        if data:
            for d in data['statuses']:
                user_mention = self.id_mention(d.get('entities'))
                reply_to = d.get('in_reply_to_user_id')

                if (user_mention == user) and (reply_to != user):
                    result_filter.append(d)
            result_filter = self.ordering_tweets(result_filter)
        return result_filter

    def ordering_tweets(self, result):
        data = sorted(result, key=lambda x: (x.get('user').get('followers_count'), x.get('retweet_count'), x.get('favorite_count')), reverse=True)

        return data

    def result_final(self, data):
        result = []
        for d in data:
            data_user = d.get('user')
            screen_name = data_user.get('screen_name')
            followers = data_user.get('followers_count')
            link = self.twitter_url + screen_name
            user = {'screen_name': screen_name, 'link': link, 'followers': followers}
            result.append({
                'user': user,
                'text': d.get('text'),
                'retweets': d.get('retweet_count'),
                'likes': d.get('favorite_count'),
                'date': d.get('created_at'),
                'link_tweet': self.tweet_url + str(d.get('id'))
            })

        return result
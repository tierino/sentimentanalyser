import config

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import pandas as pd

class TweetListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                # Exclude retweets
                if  'RT @' not in data:
                    f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, TweetListener())
    twitter_stream.filter(languages=["en"], track=["tottenham hotspur", "thfc", "tottenham"])

# # See timeline tweets
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status.text)


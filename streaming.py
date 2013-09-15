import tweepy
import json
import jsonpickle
from pprint import pprint
import os


def stream(min_time, max_tweets=100):
    # Consumer keys and access tokens, used for OAuth
    consumer_key = os.getenv('CONSUMER_KEY')
    print consumer_key
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    tweets = []
    print tweets
    for i, tweet in enumerate(tweepy.Cursor(api.search,
                                            q="#tcdisrupt",
                                            count=max_tweets,
                                            include_entities=True,
                                            lang="en").items()):
        if i >= max_tweets:
            break
        if tweet.created_at < min_time:
            continue
        tweets.append(tweet)

    # Sample method, used to update a status
    # data = api.search("#regurgitate")

    pickled = jsonpickle.encode(tweets)
    #print json.dumps(json.loads(pickled), indent=4, sort_keys=True)
    return json.dumps(json.loads(pickled), indent=4, sort_keys=True)

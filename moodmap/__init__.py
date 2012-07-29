from .utils import *
from . import twitter, sentiment
import couchdbkit

server = couchdbkit.Server("http://{0}:{1}@{2}:{3}" \
        .format(env("COUCHDB_USERNAME"),
            env("COUCHDB_PASSWORD"),
            env("COUCHDB_HOST"),
            env("COUCHDB_PORT")))

db_data = server.get_or_create_db(env("DATA_DB"))
db_tweets = server.get_or_create_db(env("TWEETS_DB"))

def _get_data():
    return db_data.view("moodmap_data/words")

def _save_tweet(id, username, tweet, latitude, longitude, timestamp, rating):
    doc = {
        "id": id,
        "username": username,
        "tweet": tweet,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp,
        "rating": rating
    }

    if not db_tweets.save_doc(doc):
        log("Failed to save doc #{0}".format(id))

def start():
    sentiment.setup(_get_data())
    twitter.start(incoming)

def clean():
    tweets = db_tweets.view("moodmap_tweets/tweets", None, None, **{
        "descending": True,
        "skip": env("TWEET_CACHE")
    })

    count = tweets.count()

    for tweet in tweets:
        db_tweets.delete_doc(tweet["id"])

    log("{0} tweets deleted".format(count))

def incoming(tweet):
    try:
        rating = sentiment.rate(tweet.text)
        if rating and not rating == 6.0:
            _save_tweet(
                tweet.id_str,
                tweet.user.screen_name,
                tweet.text,
                tweet.geo["coordinates"][0],
                tweet.geo["coordinates"][1],
                str(tweet.created_at),
                rating
            )
    except:
        pass

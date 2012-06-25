from .utils import *
import tweepy

auth = tweepy.auth.BasicAuthHandler(env("TWITTER_USERNAME"),
        env("TWITTER_PASSWORD"))

locations = [
    -14.5, 55.48, -6.34, 60.91,
    -13.96, 53.98, -5.72, 55.65,
    -8.28, 51.01, -1.08, 54.09,
    -8.66, 50.16, -1.39, 51.14,
    -9.39, 49.78, -6.53, 50.71
    ]

callback = None

class StreamWatcherListener(tweepy.StreamListener):
    def __init__(self, callback, api=None):
        self.callback = callback
        super(StreamWatcherListener, self).__init__(api)

    def on_status(self, status):
        self.callback(status)

    def on_error(self, status_code):
        log("Twitter Error: {0}".format(status_code))
        return True

    def on_timeout(self):
        log("Twitter Snoozing")

def start(callback):
    stream = tweepy.Stream(auth, StreamWatcherListener(callback))
    stream.filter(locations=locations)

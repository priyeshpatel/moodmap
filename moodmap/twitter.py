from .utils import *
import tweepy

auth = tweepy.auth.BasicAuthHandler(env("TWITTER_USERNAME"),
        env("TWITTER_PASSWORD"))

locations = [
    -7.93, 55.40, -0.53, 60.92,
    -5.65, 51.60, 2.33, 56.13,
    -5.52, 50.60, 1.67, 51.84,
    -6.64, 49.82, 1.54, 51.29, 
    -8.28, 54.07, -5.27, 55.35
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

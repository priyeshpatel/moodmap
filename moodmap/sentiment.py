import re, base64

data = {}
url_matcher = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
at_matcher = re.compile(r"([@])(\w+)\b")

def setup(words):
    for word in words:
        data[base64.b64encode(word["key"])] = word["value"]

def _tokenise(tweet):
    tweet = tweet.lower()
    tweet = tweet.replace("#", "")
    tweet = url_matcher.sub("", tweet)
    tweet = at_matcher.sub("", tweet)
    tweet = tweet.split(" ")
    return tweet

def rate(tweet):
    tweet = _tokenise(tweet)
    try:
        tweet = [base64.b64encode(x) for x in tweet]
    except:
        return False

    tokens = {}

    for x in tweet:
        if x in tokens:
            tokens[x] += 1
        else:
            tokens[x] = 1

    rating = 0.0
    count = 0

    for x in tokens:
        if x in data:
            rating += data[x] * tokens[x]
            count += tokens[x] 
    
    if count == 0:
        return 6.0

    rating /= count
            
    return rating

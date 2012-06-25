import os, sys, datetime

def env(var):
    try:
        return os.environ[var]
    except KeyError:
        sys.exit("No environment variable {0}".format(var))

def log(string):
    print "{0}: {1}".format(datetime.datetime.now().isoformat(' '), string)

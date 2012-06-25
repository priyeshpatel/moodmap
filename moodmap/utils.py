import os, sys

def env(var):
    try:
        return os.environ[var]
    except KeyError:
        sys.exit("No environment variable {0}".format(var))

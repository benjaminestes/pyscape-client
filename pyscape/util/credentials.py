import json

def load(infile):
    """From a file object, load JSON formatted keys."""

    credentials = json.load(infile)

    return (credentials['access-id'], credentials ['secret-key'],
            credentials['level'])

import os

# These values configured in Snap CI environment.
# http://www.snap-ci.com

VALID_KEYS = {
    'access_id': os.environ.get('VALID_ACCESSID'),
    'secret_key': os.environ.get('VALID_SECRETKEY')
    }

BAD_KEYS = {
    'access_id': os.environ.get('BAD_SECRETKEY'),
    'secret_key': os.environ.get('BAD_SECRETKEY')
    }
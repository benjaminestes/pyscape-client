#!/usr/bin/python3

import sys
import json
import urllib.request
import urllib.parse
import base64

class Pyscape:
    "Facilitate grabbing data from Mozscape API."
    A = 'anchor-text'
    L = 'links'
    U = 'url-metrics'

    def __init__(self, access_id, secret_key):
        self.baseurl = 'http://lsapi.seomoz.com/linkscape/' 
        auth_string = access_id + ':' + secret_key
        base64string = base64.b64encode(auth_string.encode('utf-8'))
        self.auth = base64string.decode('utf-8') 
    
    def call(self, method, url, params = None, tries = 5):
        query_string = '&'.join([k + '=' + urllib.parse.quote(str(v)) \
                                 for (k, v) in params.items()])
        
        full_query = self.baseurl + method + '/' + \
                     url + '?' + query_string

        request = urllib.request.Request(full_query)
        request.add_header("Authorization", "Basic %s" % self.auth)

        raw = urllib.request.urlopen(request)
        json_data = json.loads(raw.read().decode('utf-8'))

        return json_data

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else None

    if not url:
        exit('Invalid URL.')

    with open('keys.json', 'r') as k:
        key_string = json.load(k)

    pys = Pyscape(key_string['access-id'], key_string['secret-key'])
    print(pys.call(Pyscape.U, url))

if __name__ == '__main__':
    sys.exit(main())

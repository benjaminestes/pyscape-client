#!/usr/bin/python3

import sys
import json
import urllib.request
import urllib.parse
import base64

class Pyscape:
    "Facilitate grabbing data from Mozscape API."
    U = 'url-metrics'

    def __init__(self, access_id, secret_key):
        self.baseurl = 'http://lsapi.seomoz.com/linkscape/' 
        auth_string = access_id + ':' + secret_key
        base64string = base64.b64encode(auth_string.encode('utf-8'))
        self.auth = base64string.decode('utf-8') 
        print(auth_string)
        print(self.auth)
    
    def call(self, method, url, params = None, tries = 5):
        # If no parameters specified, choose intelligent default
        if not params:
            params = {'Cols': 137438953471}

        query_string = '&'.join([k + '=' + urllib.parse.quote(str(v)) \
                                 for (k, v) in params.items()])
        
        full_query = self.baseurl + method + '/' + \
                     url + '?' + query_string
        print(full_query)

        request = urllib.request.Request(full_query)
        request.add_header("Authorization", "Basic %s" % self.auth)

        json_data = []

        #for i in range(1, tries):
        # print('Fetching data for:', url, end='... ')
        raw = urllib.request.urlopen(request)
        json_data = json.loads(raw.read().decode('utf-8'))

        return json_data

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None
    resource = sys.argv[1] if len(sys.argv) > 1 else None
    csvfile = sys.argv[1] if len(sys.argv) > 1 else None

    with open('keys.json', 'r') as k:
        key_string = json.load(k)

    print(key_string['access-id'], key_string['secret-key'])
    
    pys = Pyscape(key_string['access-id'], key_string['secret-key'])
    print(pys.call('url-metrics', 'http://www.distilled.net'))

if __name__ == '__main__':
    sys.exit(main())

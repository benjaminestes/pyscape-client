#!/usr/bin/python3

import sys
import json
import urllib.request
import urllib.parse
import base64

class Pyscape:
    "Facilitate grabbing data from Mozscape API."
    # API call names
    A = 'anchor-text'
    L = 'links'
    U = 'url-metrics'

    # Links API scope names
    L_PTP = 'page_to_page'
    L_PTS = 'page_to_subdomain'
    L_PTD = 'page_to_domain'
    L_DTP = 'domain_to_page'
    L_DTP = 'domain_to_subdomain'
    L_DTP = 'domain_to_domain'

    # Anchor text API scope names
    A_PTP = 'phrase_to_page'
    A_PTS = 'phrase_to_subdomain'
    A_PTD = 'phrase_to_domain'
    A_TTP = 'term_to_page'
    A_TTP = 'term_to_subdomain'
    A_TTP = 'term_to_domain'

    def __init__(self, access_id, secret_key):
        self.baseurl = 'http://lsapi.seomoz.com/linkscape/' 
        auth_string = access_id + ':' + secret_key
        base64string = base64.b64encode(auth_string.encode('utf-8'))
        self.auth = base64string.decode('utf-8') 
    
    def call(self, method, url, params = None, tries = 5):
        json_data = None

        query_string = '&'.join([k + '=' + urllib.parse.quote(str(v)) \
                                 for (k, v) in params.items()])
        
        full_query = self.baseurl + method + '/' + \
                     url + '?' + query_string

        request = urllib.request.Request(full_query)
        request.add_header("Authorization", "Basic %s" % self.auth)

        try:
            raw = urllib.request.urlopen(request)
            json_data = json.loads(raw.read().decode('utf-8'))
        except:
            # Return json_data with a value None
            pass

        return json_data

    def anchor_text(self, url, scope = A_PTP):
        a_params = {'Scope': scope,
                    'Sort': 'domains_linking_page',
                    'Cols': 2}
        
        return self.call(Pyscape.A, url, a_params)

    def links(self, url, scope = L_PTP):
        data = []

        # API documentation says 50 links per request
        # is optimal
        offset = 0
        step = 50

        l_params = {'SourceCols': 4,
                    'TargetCols': 4,
                    'LinkCols': 2,
                    'Scope': scope,
                    'Sort': 'page_authority',
                    'Limit': step,
                    'Offset': offset}

        # Limited to 100,000 links total
        for i in range(int(100000 / step)):
            l_params['Offset'] = offset
            call_data = self.call(Pyscape.L, url, l_params)
            if call_data:
                # If data was received...
                data.extend(call_data)
            else:
                # If call() failed to return data, stop collecting
                break   
            offset = offset + step
        
        return data

    def url_metrics(self, url):
        u_params = {'Cols': 4}

        return self.call(Pyscape.U, url, u_params)

    def bulk_metrics(self, urls):
        data = []
        for url in urls:
            data.append(self.url_metrics(url))

        return data

def help():
    print("Placeholder.")

def main():
    method = sys.argv[1] if len(sys.argv) > 1 else None
    option1 = sys.argv[2] if len(sys.argv) > 2 else None
    option2 = sys.argv[3] if len(sys.argv) > 3 else None

    if not method:
        help()
        sys.exit()

    if not option1:
        help()
        exit('Invalid URL.')

    with open('keys.json', 'r') as k:
        key_string = json.load(k)

    pys = Pyscape(key_string['access-id'], key_string['secret-key'])
    
    if method == 'url-metrics':
        url = option1
        print(pys.url_metrics(url))
    elif method == 'bulk-metrics':
        urls = []
        with open(option1, 'r') as j:
            for line in j:
                urls.append(line.rstrip())
        print(pys.bulk_metrics(urls))
    elif method == 'links':
        url = option1
        if not option2:
            help()
            sys.exit()
        elif option2 == 'ptp':
            print(pys.links(url, Pyscape.L_PTP))
        elif option2 == 'ptd':
            print(pys.links(url, Pyscape.L_PTD))
        else:
            help()
            sys.exit()
    elif method == 'anchor-text':
        url = option1
        if not option2:
            help()
            sys.exit()
        elif option2 == 'ptp':
            print(pys.anchor_text(url, Pyscape.A_PTP))
        elif option2 == 'ptd':
            print(pys.anchor_text(url, Pyscape.A_PTD))
        else:
            help()
            sys.exit()

if __name__ == '__main__':
    sys.exit(main())

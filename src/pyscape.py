#!/usr/bin/python3

import json
import urllib.request
import urllib.parse
import base64

class Pyscape:
    "Facilitate grabbing data from Mozscape API."

    # I don't think defining all of the constants was necessary,
    # might go back and swap them out

    # API call names
    A = 'anchor-text'
    L = 'links'
    U = 'url-metrics'
    T = 'top-pages'

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
        "generates basic auth credentials"

        self.baseurl = 'http://lsapi.seomoz.com/linkscape/' 
        auth_string = access_id + ':' + secret_key
        base64string = base64.b64encode(auth_string.encode('utf-8'))
        self.auth = base64string.decode('utf-8') 
    
    def call(self, method, url, params = None, tries = 5):
        "the fundamental unit of retrieving information"

        json_data = None

        query_string = '&'.join([k + '=' + urllib.parse.quote(str(v)) \
                                 for (k, v) in params.items()])
        
        full_query = self.baseurl + method + '/' + \
                     url + '?' + query_string
        
        # Debug
        # print(full_query)

        request = urllib.request.Request(full_query)
        request.add_header("Authorization", "Basic %s" % self.auth)

        try:
            raw = urllib.request.urlopen(request)
            json_data = json.loads(raw.read().decode('utf-8'))
        except:
            # functions that call this method look for
            # an output of None to stop retrieving info
            pass

        return json_data

    def anchor_text(self, url, cols = 2, scope = A_PTP):
        "perform a call to the anchor-text API"
        
        params = {'Scope': scope,
                  'Sort': 'domains_linking_page',
                  'Cols': cols}
        
        return self.call(Pyscape.A, url, params)

    def links(self, url, t = 4, s = 4, l = 2, scope = L_PTP,
              sort = '', offset = 0, step = 50):
        "perform a call to the links API"

        params = {'SourceCols': s,
                  'TargetCols': t,
                  'LinkCols': l,
                  'Scope': scope,
                  'Sort': sort,
                  'Limit': step,
                  'Offset': offset}

        return self.call(Pyscape.L, url, params)

    def url_metrics(self, url, cols = 4):
        "perform a call to the url-metrics API"

        params = {'Cols': cols}

        # For consistency, all methods return lists that
        # can be written to CSV
        data = []
        data.append(self.call(Pyscape.U, url, params))

        return data

    def top_pages(self, url, cols = 4, offset = 0, step = 50):
        "perform a clal to the top-pages API"

        params = {'Limit': step,
                  'Offset': offset,
                  'Cols': cols}

        return self.call(Pyscape.T, url, params)

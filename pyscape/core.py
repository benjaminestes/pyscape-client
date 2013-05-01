#!/usr/bin/python3

import json
import urllib.request
import urllib.parse
import base64
import hmac
import hashlib
import time

class Pyscape:
    "Facilitate grabbing data from Mozscape API."

    # I don't think defining all of the constants was necessary,
    # might go back and swap them out
    
    # API call names
    A_CALL = 'anchor-text'
    L_CALL = 'links'
    U_CALL = 'url-metrics'
    T_CALL = 'top-pages'

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

    def __init__(self, access_id, secret_key, level):
        "generates basic auth credentials"

        self.baseurl = 'http://lsapi.seomoz.com/linkscape/' 
        auth_string = access_id + ':' + secret_key
        
        self.access_id = access_id
        self.secret_key = secret_key

        base64string = base64.b64encode(auth_string.encode('utf-8'))
        self.auth = base64string.decode('utf-8') 
        self.reporting = False
        self.set_timeout(level)

    def signature(self, expires):
        toSign  = '%s\n%i' % (self.access_id, expires)
        return base64.b64encode(hmac.new(self.secret_key.encode('ascii'), toSign.encode('ascii'), hashlib.sha1).digest())
    
    def call(self, method, url, params = None):
        "the fundamental unit of retrieving information"

        json_data = None

        # Add authentication data
        # expires = int(time.time() + 300)
        
        query_string = '&'.join([k + '=' + urllib.parse.quote(str(v)) \
                                 for (k, v) in params.items()])

        # Auth string must appear in order?
        # auth = '&AccessID=' + self.access_id + '&Expires=' + str(expires) + '&Signature=' + self.signature(expires).decode('ascii')
        
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

    def query(self, url, args):
        """Given arguments, run appropriate query."""

        # First argument returned from preset
        # handler should be method
        method = args[0]
        params = args[1:]

        if method == Pyscape.A_CALL:
            return self.query_anchor_text(url, *params)
        elif method == Pyscape.L_CALL:
            return self.query_links(url, *params)
        elif method == Pyscape.T_CALL:
            return self.query_top_pages(url, *params)
        elif method == Pyscape.U_CALL:
            return self.query_url_metrics(url, *params)
        else:
            return None

    def get_timeout(self):
        return self.timeout

    def set_timeout(self, level):
        if level == 'free':
            self.timeout = 10
        elif level == 'pro':
            self.timeout = 5
        elif level == 'full':
            self.timeout = .4
        else:
            self.timeout = .3

    def sleep(self):
        time.sleep(self.get_timeout())

    def set_reporting(self, report_mode = False):
        """Determine whether class outputs data to screen."""

        self.reporting = report_mode
    
    def report(self, *message):
        """If turned on, print reports to screen."""
        
        if self.reporting:
            print(*message, sep = '')


    def call_anchor_text(self, url, cols = 2, scope = A_PTP):
        """perform a call to the anchor-text API"""
        
        params = {'Scope': scope,
                  'Sort': 'domains_linking_page',
                  'Cols': cols}
        
        return self.call(Pyscape.A_CALL, url, params)

    def call_links(self, url, tc = 4, sc = 4, lc = 2, scope = L_PTP,
              sort = '', offset = 0, step = 50):
        "perform a call to the links API"

        params = {'SourceCols': sc,
                  'TargetCols': tc,
                  'LinkCols': lc,
                  'Scope': scope,
                  'Sort': sort,
                  'Limit': step,
                  'Offset': offset}

        return self.call(Pyscape.L_CALL, url, params)

    def call_url_metrics(self, url, cols = 4):
        "perform a call to the url-metrics API"

        params = {'Cols': cols}

        # For consistency, all methods return lists that
        # can be written to CSV
        data = []
        data.append(self.call(Pyscape.U_CALL, url, params))

        return data

    def call_top_pages(self, url, cols = 4, offset = 0, step = 50):
        "perform a call to the top-pages API"

        params = {'Limit': step,
                  'Offset': offset,
                  'Cols': cols}

        return self.call(Pyscape.T_CALL, url, params)


    def query_anchor_text(self, url, cols, scope = A_PTP):
        """run a query for anchor text"""

        self.report('Grabbing anchor text.')
        
        # anchor text query requires only one call
        return self.call_anchor_text(url, cols, scope)

    def query_links(self, url, tc, sc, lc, scope, sort):
        """run a query for call_links"""

        data = []

        # API documentation says 50 call_links per request is optimal
        offset = 0
        step = 50
        
        # Limited to 100,000 call_links total
        for i in range(int(100000 / step)):

            self.report('Grabbing URLs [', offset, ']')

            # Re-tries in case of false failure

            for j in range(5):
                self.sleep()
                call_data = self.call_links(url, tc, sc, lc, scope,
                                            sort, offset, step)

                # If there is no data, try again a few times
                if not call_data:
                    continue
                else:
                # If there is data, go to the next loop
                    break  
                    
            if call_data:
                # When exiting retry loop, determine whether there is
                # data to write
                data.extend(call_data)
                offset = offset + step
                continue
            else:
                break

        return data

    def query_top_pages(self, url, cols):
        """run a query for top pages"""

        data = []
            
        # API documentation says that 50 call_links per
        # request is optimal
        offset = 0
        step = 50

        # Limited to 10,000 URLs
        for i in range(int(10000 / step)):

            self.report('Grabbing URLs [', offset, ']')

            for j in range(5):
                self.sleep()
                call_data = self.call_top_pages(url, cols, offset, step)
                
                if not call_data:
                    continue
                else:
                    break

            if call_data:
                data.extend(call_data)
                offset = offset + step
                continue
            else:
                break   

        return data

    def query_url_metrics(self, url, cols):
        """run a query for url metrics"""

        self.report('Grabbing URL metrics.')

        return self.call_url_metrics(url, cols)

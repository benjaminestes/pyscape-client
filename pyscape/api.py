#!/usr/bin/python3

import base64
import hmac
import hashlib
import time
import requests

from .endpoints import EndpointsMixin
from .smart import SmartMixin

class Pyscape(SmartMixin, EndpointsMixin):
    "Facilitate grabbing data from Moz API."

    def __init__(self, access_id, secret_key, level):
        "generates basic auth credentials"
        self.api_url = 'http://lsapi.seomoz.com/linkscape/'         
        self.access_id = access_id
        self.secret_key = secret_key
        
    def __repr__(self):
        return '<Pyscape: %s>' % (self.access_id)

    def get_signature(self, expires):
        toSign  = '%s\n%i' % (self.access_id, expires)
        return base64.b64encode(hmac.new(self.secret_key.encode('ascii'), toSign.encode('ascii'), hashlib.sha1).digest())
    
    def get(self, endpoint, url = '', params = {}):
        "the fundamental unit of retrieving information. returns none if no response."
        
        expires = int(time.time() + 300)
        params['AccessID'] = self.access_id
        params['Expires'] = expires
        params['Signature'] = self.get_signature(expires)

        call = ''.join([self.api_url, endpoint, '/', url])
        
        response = requests.get(call, params = params)
        
        self._last_call = {
            'endpoint': endpoint,
            'url': url,
            'call': response.url,
            'headers': response.headers,
            'status': response.status_code,
            'content': response.text,
        }

        return response.json()
        
    def get_last_call_header(self, header):
        return self._last_call['headers'][header]
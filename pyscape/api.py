#!/usr/bin/python3

import base64
import hashlib
import hmac
import json
import requests
import time

from .endpoints import EndpointsMixin
from .defaults import DEFAULTS
from .fields import FIELDS

class Pyscape(EndpointsMixin):
    "Facilitate grabbing data from Moz API."

    def __init__(self, access_id, secret_key, level):
        "generates basic auth credentials"
        self.api_url = 'http://lsapi.seomoz.com/linkscape/'         
        self.access_id = access_id
        self.secret_key = secret_key
        
    def __repr__(self):
        return '<Pyscape: %s>' % (self.access_id)

    def _add_signature(self, params = {}):
        expires = int(time.time() + 300)
        toSign  = '%s\n%i' % (self.access_id, expires)

        params['AccessID'] = self.access_id
        params['Expires'] = expires
        params['Signature'] = base64.b64encode(hmac.new(self.secret_key.encode('ascii'), toSign.encode('ascii'), hashlib.sha1).digest())

        return params
    
    def get(self, endpoint, url = '', params = {}):
        "the fundamental unit of retrieving information. returns none if no response."
        params = self._add_signature(params)
        
        # Filters are passed as a list, but need to be separated
        # with '+' when put in URL.
        if 'Filters' in params:
            params['Filters'] = '+'.join(params['Filters'])
             
        call = ''.join([self.api_url, endpoint, '/', url])

        return requests.get(call, params = params)
    
    def post(self, endpoint, urls = [], params = {}):
        "Filters don't apply to url-metrics."
        params = self._add_signature(params)
        
        call = ''.join([self.api_url, endpoint, '/'])
        
        return requests.post(call, params = params, data=json.dumps(urls))
        
    def _get_bitflag(self, field):
        return FIELD_INDEX[field]['flag']
        
    def _add_smart_fields(self, endpoint, params = {}):
    
        if all(k not in params for k in ['Cols','SourceCols','TargetCols','LinkCols']):
            # Shortcut for readability
            field_groups = DEFAULTS[endpoint][params['Scope']]['Fields']
            for group in field_groups:
                bit_field = 0
                for field in field_groups[group]:
                    bit_field = bit_field | self._get_bitflag(field)
                params[group] = bit_field
        
        if 'Sort' in DEFAULTS[endpoint][params['Scope']] and 'Sort' not in params:
            params['Sort'] = DEFAULTS[endpoint][params['Scope']]['Sort']

        return params
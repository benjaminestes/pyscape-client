#!/usr/bin/python3

from pyscape import Pyscape
import unittest
import json

class TestCall(unittest.TestCase):

    def setUp(self):
        self.a_params = {'Scope': 'phrase_to_page',
                         'Sort': 'domains_linking_page',
                         'Cols': 2}
        self.l_params = {'SourceCols': 4,
                         'TargetCols': 4,
                         'LinkCols': 2,
                         'Scope': 'page_to_domain',
                         'Sort': 'page_authority',
                         'Limit': 5,
                         'Offset': 0}
        self.u_params = {'Cols': 4}
        self.url = 'www.distilled.net'

        with open('keys.json', 'r') as k:
            key_string = json.load(k)

        self.pys = Pyscape(key_string['access-id'],
                           key_string['secret-key'])

    def test_acall(self):
        self.pys.call(Pyscape.A, self.url, self.a_params)

    def test_lcall(self):
        self.pys.call(Pyscape.L, self.url, self.l_params)

    def test_ucall(self):
        self.pys.call(Pyscape.U, self.url, self.u_params)

if __name__ == '__main__':
    unittest.main()

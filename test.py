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
        a = self.pys.call(Pyscape.A, self.url, self.a_params)
        b = self.pys.anchor_text(self.url)
        self.assertEqual(a, b)

    def test_atype(self):
        a = self.pys.call(Pyscape.A, self.url, self.a_params)
        self.assertIsInstance(type(a), list)

    def test_lcall(self):
        # should now fail since links() uses multiple calls
        a = self.pys.call(Pyscape.L, self.url, self.l_params)
        b = self.pys.links(self.url)
        self.assertEqual(a, b)

    def test_ucall(self):
        a = self.pys.call(Pyscape.U, self.url, self.u_params)
        b = self.pys.url_metrics(self.url)
        self.assertEqual(a, b)

    def test_offset(self):
        # test step feature combining link return data
        # assumes 3 requests, limit 5 each, for 15 total
        self.assertEqual(len(self.pys.links(self.url)),15)

if __name__ == '__main__':
    unittest.main()

#! /usr/bin/env/ python3

import unittest

from pyscape import Pyscape

from config import VALID_KEYS

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.p = Pyscape(**VALID_KEYS)
        
    def test_get_url_metrics(self):
        r = self.p.get_url_metrics('distilled.net')
        return self.assertEqual('distilled.net/', r.json()['uu'])
    
    def test_get_anchor_text(self):
        r = self.p.get_anchor_text('distilled.net')
        return self.assertTrue('aput' in r.json()[0])
        
    def test_get_links(self):
        r = self.p.get_links('distilled.net')
        return self.assertTrue('luuu' in r.json()[0])
        
    def test_get_top_pages(self):
        r = self.p.get_anchor_text('distilled.net')
        return self.assertTrue('uu' in r.json()[0])

if __name__ == '__main__':
    unittest.main()
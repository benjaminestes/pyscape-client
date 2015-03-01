#! /usr/bin/env/ python3

import unittest

from pyscape import Pyscape

from config import VALID_KEYS

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.p = Pyscape(**VALID_KEYS)
        pass
        
    def test_call_format(self):
        pass

if __name__ == '__main__':
    unittest.main()
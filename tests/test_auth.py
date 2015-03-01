#! /usr/bin/env/ python3

import unittest

from pyscape import Pyscape

from config import VALID_KEYS, BAD_KEYS

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        valid_instance = Pyscape(**VALID_KEYS)
        bad_instance = Pyscape(**BAD_KEYS)
        pass

if __name__ == '__main__':
    unittest.main()
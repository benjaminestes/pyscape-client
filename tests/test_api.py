#! /usr/bin/env/ python3

from pyscape import Pyscape

from .config import VALID_KEYS

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        p = Pyscape(**VALID_KEYS)
        pass

if __name__ == '__main__':
    unittest.main()
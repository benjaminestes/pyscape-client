#! /usr/bin/env/ python3

import os
import unittest
import sys

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        p = Pyscape(os.environ.get('PYSCAPE_ACCESSID'),
                    os.environ.get('PYSCAPE_SECRETKEY'))
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
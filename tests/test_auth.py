#! /usr/bin/env/ python3

import unittest

from pyscape import Pyscape

from config import VALID_KEYS, BAD_KEYS

class PyscapeAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_instance = Pyscape(**VALID_KEYS)
        self.bad_instance = Pyscape(**BAD_KEYS)

    def test_auth_success(self):
        """Test something."""
        self.assertEqual(200, self.valid_instance.get_index_stats().status_code)
    
    def test_auth_fail(self):
        """Test something."""
        self.assertEqual(403, self.bad_instance.get_index_stats().status_code)

if __name__ == '__main__':
    unittest.main()
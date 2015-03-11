import os
import unittest
from pyscape import Pyscape

# These values configured in Snap CI environment.
# http://www.snap-ci.com

VALID_KEYS = {
    'access_id': os.environ.get('VALID_ACCESSID'),
    'secret_key': os.environ.get('VALID_SECRETKEY')
    }

BAD_KEYS = {
    'access_id': os.environ.get('BAD_SECRETKEY'),
    'secret_key': os.environ.get('BAD_SECRETKEY')
    }

class PyscapeAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_instance = Pyscape(**VALID_KEYS)
        self.bad_instance = Pyscape(**BAD_KEYS)

    def test_auth_success(self):
        """Test something."""
        self.assertEqual(200, self.valid_instance.get_index_stats().status_code)
    
    def test_auth_fail(self):
        """Test something."""
        self.assertEqual(401, self.bad_instance.get_index_stats().status_code)
    
    def test_get_url_metrics(self):
        r = self.valid_instance.get_url_metrics('distilled.net')
        return self.assertEqual('distilled.net/', r.json()['uu'])
    
    def test_get_anchor_text(self):
        r = self.valid_instance.get_anchor_text('distilled.net')
        return self.assertTrue('aput' in r.json()[0])
        
    def test_get_links(self):
        r = self.valid_instance.get_links('distilled.net')
        return self.assertTrue('luuu' in r.json()[0])
        
    def test_get_top_pages(self):
        r = self.valid_instance.get_top_pages('distilled.net')
        return self.assertTrue('uu' in r.json()[0])

if __name__ == '__main__':
    unittest.main()
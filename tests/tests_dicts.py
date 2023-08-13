import unittest
from utils import dicts

class Test_dict(unittest.TestCase):
    def test_get_val(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs"), ('mercurial'))
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), ('mercurial'))
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), ('bazaar'))

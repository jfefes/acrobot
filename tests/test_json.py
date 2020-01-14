""" test for valid json """
import json
import unittest


class TestJsonValidity(unittest.TestCase):
    def test_json_to_dict(self):
        # tests that json is valid
        with open('acronyms.json') as json_file:
            acronyms = json.load(json_file)

        self.assertTrue(type(acronyms), dict)

    def test_json_unique_keys(self):
        with open('acronyms.json') as json_file:
            json.load(json_file, object_pairs_hook=dict_raise_on_duplicates)


def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate key: %r" % (k,))
        else:
            d[k] = v
    return d

"""tests for immutability"""

from unittest import TestCase

from test import SuperNested


class TestImmutable(TestCase):

    def test_cannot_set_item(self):
        with self.assertRaises(AttributeError):
            SuperNested()['database'] = 1

    def test_cannot_set_attriute(self):
        with self.assertRaises(AttributeError):
            SuperNested().database = 1

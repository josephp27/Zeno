"""tests for immutability"""

from unittest import TestCase

from ZenoMapper.zeno import Zeno
from test import SuperNested


class TestImmutable(TestCase):

    def test_cannot_set_item(self):
        with self.assertRaises(AttributeError):
            SuperNested()['database'] = 1

    def test_cannot_set_attriute(self):
        with self.assertRaises(AttributeError):
            SuperNested().database = 1

    def test_cannot_set_item_zeno(self):
        with self.assertRaises(AttributeError):
            Zeno()['Spring'] = 1

    def test_cannot_set_attriute_zeno(self):
        with self.assertRaises(AttributeError):
            Zeno().Spring = 1

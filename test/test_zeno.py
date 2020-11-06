"""tests for immutability"""

from unittest import TestCase

from ZenoMapper.zeno import Zeno
from test import parsed_yml


class TestZeno(TestCase):
    def test_zeno_is_equal_dictionary_when_nothing_set_in_constructor(self):
        self.assertEqual(Zeno(), parsed_yml)

    def test_zeno_is_equal_dictionary(self):
        self.assertEqual(Zeno('Spring'), parsed_yml['Spring'])

    def test_zeno_is_equal_dictionary_referencing_first_nested(self):
        self.assertEqual(Zeno('Spring').Data, parsed_yml['Spring']['Data'])

    def test_zeno_is_equal_dictionary_referencing_second_nested(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb'), parsed_yml['Spring']['Data']['MongoDb'])

    def test_zeno_is_equal_dictionary_referencing_third_nested(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').Nested, parsed_yml['Spring']['Data']['MongoDb']['Nested'])

    def test_zeno_nested_loads_list(self):
        self.assertEqual(Zeno('Spring').Data.myList, ['first', 'second', 'third'])

    def test_zeno_nested_loads_second_first_nested(self):
        self.assertEqual(Zeno('Spring').Data.second, 1)

    def test_zeno_nested_loads_nested_dot_notation_db(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').database, 'TESTDB')

    def test_zeno_nested_loads_nested_dot_notation_encryption(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').encryption, True)

    def test_zeno_nested_loads_nested_dot_notation_enckey(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').encryptionKey, 'FakePassWord!')

    def test_zeno_nested_loads_nested_dot_notation_pass(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').password, '!54353Ffesf34')

    def test_zeno_nested_loads_nested_dot_notation_replica(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').replicaSet, 'FAKE-DB-531')

    def test_zeno_nested_loads_nested_dot_notation_nested_key(self):
        self.assertEqual(Zeno('Spring.Data.MongoDb').Nested.key, 5243)

"""Configuration for tests"""

from unittest import TestCase

from test import Spring, parsed_yml, SuperNested, MyServer, Lower


class TestNested(TestCase):
    def test_is_equal_dictionary(self):
        self.assertEqual(Spring(), parsed_yml['Spring'])

    def test_is_equal_dictionary_referencing_first_nested(self):
        self.assertEqual(Spring().Data, parsed_yml['Spring']['Data'])

    def test_is_equal_dictionary_referencing_second_nested(self):
        self.assertEqual(Spring().Data.MongoDb, parsed_yml['Spring']['Data']['MongoDb'])

    def test_is_equal_dictionary_referencing_third_nested(self):
        self.assertEqual(Spring().Data.MongoDb.Nested, parsed_yml['Spring']['Data']['MongoDb']['Nested'])

    def test_nested_loads_list(self):
        self.assertEqual(Spring().Data.myList, ['first', 'second', 'third'])

    def test_nested_loads_second_first_nested(self):
        self.assertEqual(Spring().Data.second, 1)

    def test_nested_loads_nested_dot_notation_db(self):
        self.assertEqual(Spring().Data.MongoDb.database, 'TESTDB')

    def test_nested_loads_nested_dot_notation_encryption(self):
        self.assertEqual(Spring().Data.MongoDb.encryption, True)

    def test_nested_loads_nested_dot_notation_enckey(self):
        self.assertEqual(Spring().Data.MongoDb.encryptionKey, 'FakePassWord!')

    def test_nested_loads_nested_dot_notation_pass(self):
        self.assertEqual(Spring().Data.MongoDb.password, '!54353Ffesf34')

    def test_nested_loads_nested_dot_notation_replica(self):
        self.assertEqual(Spring().Data.MongoDb.replicaSet, 'FAKE-DB-531')

    def test_nested_loads_nested_dot_notation_nested_key(self):
        self.assertEqual(Spring().Data.MongoDb.Nested.key, 5243)


class TestSuperNested(TestCase):
    def test_SuperNested_section_skips_needing_to_nest_classes_db(self):
        self.assertEqual(SuperNested().database, 'TESTDB')

    def test_SuperNested_section_skips_needing_to_nest_classes_encryption(self):
        self.assertEqual(SuperNested().encryption, True)

    def test_SuperNested_section_skips_needing_to_nest_classes_enckey(self):
        self.assertEqual(SuperNested().encryptionKey, 'FakePassWord!')

    def test_SuperNested_section_skips_needing_to_nest_classes_pass(self):
        self.assertEqual(SuperNested().password, '!54353Ffesf34')

    def test_SuperNested_section_skips_needing_to_nest_classes_replica(self):
        self.assertEqual(SuperNested().replicaSet, 'FAKE-DB-531')

    def test_SuperNested_section_skips_needing_to_nest_classes_nested_key(self):
        self.assertEqual(SuperNested().Nested.key, 5243)


class TestModifyConfig(TestCase):
    def test_MyServer_has_one_attribute_when_only_one_specified(self):
        self.assertEqual(MyServer(), {'host': 'my.server.com'})


class TestGetDictionaries(TestCase):
    def test_can_find_key_if_lower(self):
        self.assertEqual(Lower(), {'CaseSection': True})

    def test_can_find_key_if_CamelCase(self):
        self.assertEqual(Lower().CaseSection, True)

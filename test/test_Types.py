from unittest import TestCase

from ZenoMapper import Integer, List, Boolean, String


class TestInteger(TestCase):
    def test_convert_converts_integer(self):
        actual = Integer().convert(183)

        self.assertEqual(actual, 183)

    def test_convert_converts_string(self):
        actual = Integer().convert("183")

        self.assertEqual(actual, 183)


class TestList(TestCase):
    def test_convert_converts_list(self):
        actual = List().convert([])

        self.assertEqual(actual, [])

    def test_convert_converts_empty_string(self):
        actual = List().convert('')

        self.assertEqual(actual, [])

    def test_convert_converts_empty_list(self):
        actual = List().convert('[]')

        self.assertEqual(actual, [])

    def test_convert_converts_list_with_braces(self):
        actual = List().convert('[first, second, third]')

        self.assertEqual(actual, ['first', 'second', 'third'])

    def test_convert_converts_list_without_braces(self):
        actual = List().convert('first, second, third')

        self.assertEqual(actual, ['first', 'second', 'third'])

    def test_convert_throws_exception_when_not_string_or_list(self):
        with self.assertRaises(Exception) as context:
            List().convert(543234)

        self.assertTrue('543234 is not a string or list' in str(context.exception))


class TestBoolean(TestCase):
    def test_convert_converts_boolean_True(self):
        actual = Boolean().convert(True)

        self.assertEqual(actual, True)

    def test_convert_converts_boolean_False(self):
        actual = Boolean().convert(False)

        self.assertEqual(actual, False)

    def test_convert_converts_string_yes(self):
        actual = Boolean().convert('yes')

        self.assertEqual(actual, True)

    def test_convert_converts_string_yes_different_case(self):
        actual = Boolean().convert('YES')

        self.assertEqual(actual, True)

    def test_convert_converts_string_true(self):
        actual = Boolean().convert('true')

        self.assertEqual(actual, True)

    def test_convert_converts_string_t(self):
        actual = Boolean().convert('t')

        self.assertEqual(actual, True)

    def test_convert_converts_string_one(self):
        actual = Boolean().convert('1')

        self.assertEqual(actual, True)

    def test_convert_converts_string_false(self):
        actual = Boolean().convert('false')

        self.assertEqual(actual, False)

    def test_convert_converts_string_not_yes_true_t_1(self):
        actual = Boolean().convert('fjkdsla;')

        self.assertEqual(actual, False)

    def test_convert_throws_exception_when_not_string(self):
        with self.assertRaises(Exception) as context:
            Boolean().convert(543234)

        self.assertTrue('Invalid literal for boolean. Not a string: 543234' in str(context.exception))


class TestString(TestCase):
    def test_converts_string(self):
        actual = String().convert(183)

        self.assertEqual(actual, "183")

    def test_converts_list(self):
        actual = String().convert([])

        self.assertEqual(actual, "[]")

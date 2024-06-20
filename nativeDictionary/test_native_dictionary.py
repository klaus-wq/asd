import unittest
from native_dictionary import *

class TestNativeDictionary(unittest.TestCase):
    def test_hash_fun(self):
        hash_table = NativeDictionary(17)
        str = hash_table.hash_fun('Hello')
        self.assertEqual(True, str < 17)
        str1 = hash_table.hash_fun("Hello, world!  ")
        self.assertEqual(True, str1 < 17)
        str2 = hash_table.hash_fun('/123.  ')
        self.assertTrue(True, str2 < 17)

    def test_put(self):
        native_dictionary = NativeDictionary(17)
        native_dictionary.put("1", "1")
        native_dictionary.put("2", "2")
        native_dictionary.put("3", "3")
        native_dictionary.put("4", "4")
        print(native_dictionary.slots, native_dictionary.values)
        self.assertTrue(native_dictionary.is_key("1"))
        self.assertTrue(native_dictionary.is_key("2"))
        self.assertTrue(native_dictionary.is_key("3"))
        self.assertTrue(native_dictionary.is_key("4"))
        self.assertEqual(native_dictionary.put("1", "5"), None)
        self.assertEqual(native_dictionary.slots.index("2"), native_dictionary.values.index("2"))
        self.assertEqual(native_dictionary.slots.index("3"), native_dictionary.values.index("3"))

    def test_is_key(self):
        native_dictionary = NativeDictionary(17)
        native_dictionary.put("1", "1")
        self.assertTrue(native_dictionary.is_key("1"))
        self.assertFalse(native_dictionary.is_key("5"))

    def test_get(self):
        native_dictionary = NativeDictionary(17)
        native_dictionary.put("1", "1")
        native_dictionary.put("2", "2")
        native_dictionary.put("3", "3")
        native_dictionary.put("4", "4")
        self.assertEqual(native_dictionary.get("1"), "1")
        self.assertEqual(native_dictionary.get("2"), "2")
        self.assertEqual(native_dictionary.get("3"), "3")
        self.assertEqual(native_dictionary.get("4"), "4")
        self.assertEqual(native_dictionary.get("5"), None)


if __name__ == '__main__':
    unittest.main()
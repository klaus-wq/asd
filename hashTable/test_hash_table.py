import unittest

from hash_table import *


class TestHashTable(unittest.TestCase):
    def test_hash_func(self):
        hash_table = HashTable(17, 3)
        str = hash_table.hash_fun('Hello')
        self.assertEqual(True, str < 17)
        str1 = hash_table.hash_fun("Hello, world!  ")
        self.assertEqual(True, str1 < 17)
        str2 = hash_table.hash_fun('/123.  ')
        self.assertTrue(True, str2 < 17)

    def test_seek_slot(self):
        hash_table = HashTable(5, 3)
        hash_table.slots[0] = "1"
        hash_table.slots[4] = "2"
        hash_table.slots[2] = "3"
        hash_table.slots[3] = "4"
        self.assertEqual(hash_table.seek_slot("5"), 1)
        hash_table.put("5")
        self.assertEqual(hash_table.seek_slot("6"), None)

    def test_put(self):
        hash_table = HashTable(17, 3)
        for i in range(17):
            hash_table.put('hello')
        self.assertEqual(hash_table.put('world'), None)
        hash_table = HashTable(17, 3)
        index = hash_table.put('world')
        self.assertEqual(hash_table.slots[index], 'world')

    def test_find(self):
        hash_table = HashTable(17, 3)
        for i in range(17):
            hash_table.put(str(i))
        self.assertEqual(hash_table.slots[hash_table.find("15")], "15")
        self.assertEqual(hash_table.find("20"), None)


if __name__ == '__main__':
    unittest.main()

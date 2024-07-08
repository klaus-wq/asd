import unittest
from native_cache import *

class TestNativeCache(unittest.TestCase):

	def test_hash_fun(self):
		cache = NativeCache(17)
		str = cache.hash_fun('Hello')
		self.assertEqual(True, str < 17)
		str1 = cache.hash_fun("Hello, world!  ")
		self.assertEqual(True, str1 < 17)
		str2 = cache.hash_fun('/123.  ')
		self.assertTrue(True, str2 < 17)

	def test_put(self):
		cache = NativeCache(17)
		key = 'key'
		value = 'value'
		cache.put(key, value, 3)
		self.assertTrue(key in cache.slots)
		self.assertTrue(value in cache.values)
		self.assertEqual(cache.slots.index(key), cache.values.index(value))
		index = cache.hash_fun(key)
		self.assertEqual(cache.values[index], value)
		self.assertEqual(cache.slots[index], key)
		value_2 = "value_2"
		cache.put(key, value_2, 3)
		self.assertTrue(value not in cache.values)
		self.assertTrue(value_2 in cache.values)
		self.assertEqual(cache.slots.index(key), cache.values.index(value_2))
		index = cache.hash_fun(key)
		self.assertEqual(cache.values[index], value_2)
		for i in range(17):
			cache.put(i, i, 3)
		hits_index = cache.hits.index(min(cache.hits))
		key_2 = "key_2"
		value_3 = "value_3"
		cache.put(key_2, value_3, 3)
		self.assertTrue(key_2 in cache.slots)
		self.assertTrue(value_3 in cache.values)
		self.assertEqual(cache.slots.index(key_2), cache.values.index(value_3))
		self.assertEqual(cache.slots.index(key_2), hits_index)

	def test_is_key(self):
		cache = NativeCache(17)
		key = 'key'
		value = 'value'
		self.assertFalse(cache.is_key(key))
		cache.put(key, value, 3)
		self.assertTrue(cache.is_key(key))

	def test_get(self):
		cache = NativeCache(17)
		key = 'key'
		value = 'value'
		self.assertEqual(cache.get(key), None)
		cache.put(key, value, 3)
		self.assertEqual(cache.get(key), value)
		self.assertEqual(cache.hits[cache.slots.index(key)], 1)


if __name__ == '__main__':
	unittest.main()
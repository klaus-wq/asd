import unittest
from bloom_filter import *

strings = ["0123456789", "1234567890", "2345678901", "3456789012", "4567890123", "5678901234", "6789012345",
          "7890123456","8901234567","9012345678"]

class TestBloomFilter(unittest.TestCase):
    def test_bloom(self):
        bloom_filter = BloomFilter(32)
        for i in strings:
            self.assertFalse(bloom_filter.is_value(i))
            self.assertTrue(
                bloom_filter.hash1(i) >= 0 and
                bloom_filter.hash1(i) < bloom_filter.filter_len
            )
            self.assertTrue(
                bloom_filter.hash2(i) >= 0 and
                bloom_filter.hash2(i) < bloom_filter.filter_len
            )
        for i in strings:
            bloom_filter.add(i)
            self.assertTrue(bloom_filter.is_value(i))

if __name__ == '__main__':
    unittest.main()
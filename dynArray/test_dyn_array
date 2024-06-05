import unittest

from dyn_array import *


class TestDynamicArray(unittest.TestCase):
    def test_insert(self):
        dynArray = DynArray()
        dynArray.insert(0, 5)
        dynArray.insert(1, 6)
        dynArray.insert(2, 7)
        self.assertEqual(dynArray.count, 3)
        self.assertEqual(dynArray.capacity, 16)
        self.assertEqual(dynArray[dynArray.count - 1], 7)
        self.assertEqual(dynArray[0], 5)
        for i in range(15):
            dynArray.append(i)
        self.assertEqual(dynArray.count, 18)
        self.assertEqual(dynArray.capacity, 32)
        self.assertEqual(dynArray[dynArray.count - 1], 14)
        self.assertEqual(dynArray[0], 5)
        try:
            dynArray.insert(20, 10)
        except IndexError as e:
            self.assertEqual(
                str(e), 'Index is out of bounds'
            )
    
    def test_delete(self):
        dynArray = DynArray()
        dynArray.append(0)
        dynArray.append(1)
        dynArray.append(2)
        dynArray.append(3)
        dynArray.delete(1)
        self.assertEqual(dynArray.count, 3)
        self.assertEqual(dynArray.capacity, 16)
        self.assertEqual(dynArray[dynArray.count - 1], 3)
        self.assertEqual(dynArray[0], 0)
        dynArray = DynArray()
        for i in range(18):
            dynArray.append(i)
        self.assertEqual(dynArray.count, 18)
        self.assertEqual(dynArray.capacity, 32)
        dynArray.delete(0)
        dynArray.delete(0)
        dynArray.delete(0)
        dynArray.delete(0)
        dynArray.delete(0)
        self.assertEqual(dynArray.count, 13)
        self.assertEqual(dynArray.capacity, 21)
        self.assertEqual(dynArray[dynArray.count - 1], 17)
        self.assertEqual(dynArray[0], 5)
        try:
            dynArray.delete(50)
        except IndexError as e:
            self.assertEqual(
                str(e), 'Index is out of bounds'
            )
        

if __name__ == '__main__':
    unittest.main()

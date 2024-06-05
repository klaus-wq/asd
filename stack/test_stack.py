import unittest

from stack import *


class TestStack(unittest.TestCase):
    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        for i in range(5):
            stack.push(1)
        self.assertEqual(stack.size(), 5)
    
    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.stack[0], 5)
        stack.push(10)
        stack.push(11)
        self.assertEqual(stack.stack[0], 11)
        self.assertEqual(stack.stack[stack.size() - 1], 5)
    
    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), 4)
    
    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), 4)

if __name__ == '__main__':
    unittest.main()

import unittest
from queue import *

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(50)
        self.assertEqual(queue.queue[len(queue.queue) - 1], 50)
        queue.enqueue(60)
        queue.enqueue(70)
        self.assertEqual(queue.queue[len(queue.queue) - 1], 70)

    def test_dequeue(self):
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)
        queue.enqueue(50)
        self.assertEqual(queue.dequeue(), 50)
        queue.enqueue(60)
        queue.enqueue(70)
        self.assertEqual(queue.dequeue(), 60)
        self.assertEqual(queue.dequeue(), 70)
        self.assertEqual(queue.dequeue(), None)

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        queue.enqueue(50)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(60)
        queue.enqueue(70)
        self.assertEqual(queue.size(), 3)

if __name__ == '__main__':
    unittest.main()
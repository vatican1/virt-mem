import unittest

from virtual_memory import FIFO_algo, read_sequence


class TestVirtMemory(unittest.TestCase):
    def test_read_sequence(self):
        N, M, list_of_pages = read_sequence('data/sequence_example.txt')
        self.assertEqual(N, 10)
        self.assertEqual(M, 5)
        self.assertEqual(list_of_pages, [5, 6, 7, 10, 5, 7, 10, 5, 9])

    def test_FIFO_algo(self):
        N, M, list_of_pages = read_sequence('data/sequence_example.txt')

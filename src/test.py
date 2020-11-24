import unittest

from virtual_memory import fifo_algo, read_sequence, lru_algo, opt_algo


class TestVirtMemory(unittest.TestCase):
    def test_read_sequence(self):
        n, m, list_of_pages = read_sequence('data/sequence_example.txt')
        self.assertEqual(n, 10)
        self.assertEqual(m, 5)
        self.assertEqual(list_of_pages, [5, 6, 7, 10, 5, 7, 10, 5, 9])

    def test_FIFO_algo(self):
        n, m, list_of_pages = read_sequence('data/example.txt')
        self.assertEqual(fifo_algo(m, list_of_pages), 16)

    def test_LRU_algo(self):
        n, m, list_of_pages = read_sequence('data/example.txt')
        self.assertEqual(lru_algo(m, list_of_pages), 16)

    def test_OPT_algo(self):
        n, m, list_of_pages = read_sequence('data/example.txt')
        self.assertEqual(opt_algo(m, list_of_pages), 10)

import unittest
from BagsTracker import find_max_dist


class BagsTracker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_max_dist(8, 9, 3), 3)

    def test_2(self):
        self.assertEqual(find_max_dist(12, 18, 5), 4)

    def test_3(self):
        self.assertEqual(find_max_dist(67, 100, 24), 5)


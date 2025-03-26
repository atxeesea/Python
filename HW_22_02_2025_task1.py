import unittest

class NumberSet:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def sum(self):
        return sum(self.numbers)
    
    def average(self):
        return self.sum() / len(self.numbers) if self.numbers else 0
    
    def max(self):
        return max(self.numbers) if self.numbers else None
    
    def min(self):
        return min(self.numbers) if self.numbers else None


class TestNumberSet(unittest.TestCase):
    nums = NumberSet([2, 4, 6, 8, 10])
    
    def test_sum(self):
        self.assertEqual(self.nums.sum(), 30)
    
    def test_average(self):
        self.assertEqual(self.nums.average(), 6)
    
    def test_max(self):
        self.assertEqual(self.nums.max(), 10)
    
    def test_min(self):
        self.assertEqual(self.nums.min(), 2)

unittest.main()
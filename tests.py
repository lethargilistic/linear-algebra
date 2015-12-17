from linear import *
import unittest

class TestModule(unittest.TestCase):
    def test_addition_valid(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        b = [[1,2,3],[4,5,6],[7,8,9]]
        answer = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        result = addition(a, b)
        self.assertEqual(result, answer)

    
    def test_subtraction_valid(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        b = [[1,2,3],[4,5,6],[7,8,9]]
        answer = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = subtraction(a, b)
        self.assertEqual(result, answer)
        
if __name__ == "__main__":
    unittest.main()

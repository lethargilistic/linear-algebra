from linear import linear as lin
import unittest

class TestModule(unittest.TestCase):
    def test_addition_valid(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        answer = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        result = lin.addition(a, b)
        self.assertEqual(result, answer)

    def test_subtraction_valid(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        answer = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = lin.subtraction(a, b)
        self.assertEqual(result, answer)

    def test_multiplication_valid(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        answer = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
        result = lin.multiplication(a, b)
        self.assertEqual(result, answer)

    def test_exponent_valid_square(self):
        a = [[2, 0, 0], [0, 3, 0], [0, 0, 4]]
        power = 3
        answer = [[8, 0, 0], [0, 27, 0], [0, 0, 64]]
        result = lin.exponent(a, power)
        self.assertEqual(result, answer)
        
    def test_is_diagonal_true(self):
        a = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
        self.assertTrue(lin.is_diagonal(a))

    def test_is_diagonal_false(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(lin.is_diagonal(a))
        
    def test_is_identity_true(self):
        a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertTrue(lin.is_identity(a))

    def test_is_identity_false(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(lin.is_identity(a))

    def test_are_same_size_true(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        self.assertTrue(lin.are_same_size(a, b))
        
    def test_are_same_size_false_from_rows(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8, 7], [6, 5, 4]]
        self.assertFalse(lin.are_same_size(a, b))

    def test_are_same_size_false_from_cols(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8], [6, 5], [3, 2]]
        self.assertFalse(lin.are_same_size(a, b))

    def test_are_transposed_true(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertTrue(lin.are_transposed(a,b))
        
    def test_are_transposed_false(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertFalse(lin.are_transposed(a,b))
        
if __name__ == "__main__":
    unittest.main()

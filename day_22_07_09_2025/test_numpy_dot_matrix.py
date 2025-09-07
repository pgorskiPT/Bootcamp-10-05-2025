# wygenerował coopilot
import unittest

from day_22_07_09_2025.numpy_dot_matrix import multiply_python_arrays


class TestMultiplyPythonArrays(unittest.TestCase):
    def test_identity_matrix(self):
        x = [
            [1.0, 0.0],
            [0.0, 1.0]
        ]
        y = [
            [5.0, 6.0],
            [7.0, 8.0]
        ]
        expected = [
            [5.0, 6.0],
            [7.0, 8.0]
        ]
        result = multiply_python_arrays(x, y)
        self.assertEqual(result, expected)

    def test_square_matrices(self):
        x = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]
        y = [
            [5.0, 6.0],
            [7.0, 8.0]
        ]
        expected = [
            [19.0, 22.0],
            [43.0, 50.0]
        ]
        result = multiply_python_arrays(x, y)
        self.assertEqual(result, expected)

    def test_rectangular_matrices(self):
        x = [
            [1.0, 2.0, 3.0]
        ]
        y = [
            [4.0],
            [5.0],
            [6.0]
        ]
        expected = [
            [32.0]
        ]
        result = multiply_python_arrays(x, y)
        self.assertEqual(result, expected)

    def test_zero_matrix(self):
        x = [
            [0.0, 0.0],
            [0.0, 0.0]
        ]
        y = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]
        expected = [
            [0.0, 0.0],
            [0.0, 0.0]
        ]
        result = multiply_python_arrays(x, y)
        self.assertEqual(result, expected)

    def test_incompatible_shapes(self):
        x = [
            [1.0, 2.0]
        ]
        y = [
            [3.0, 4.0],
            [5.0, 6.0],
            [7.0, 8.0]
        ]
        with self.assertRaises(IndexError):
            multiply_python_arrays(x, y)


if __name__ == "__main__":
    unittest.main()

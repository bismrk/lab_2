import unittest
import main

class TestBubbleSort(unittest.TestCase):
    def test_Empty(self):
        expected = []
        x = main.Array([]).bubbleSort()
        self.assertEqual(expected, x)

    def test_The_Same(self):
        expect = [0, 0, 0]
        x = main.Array([0, 0, 0]).bubbleSort()
        self.assertEqual(expect, x)

    def test_Double(self):
        expect = [0.01, 0.5, 1.5]
        x = main.Array([1.5, 0.01, 0.5]).bubbleSort()
        self.assertEqual(expect, x)

    def test_Neg(self):
        expect = [-1.5, -0.01, 0.5]
        x = main.Array([-1.5, 0.5, -0.01]).bubbleSort()
        self.assertEqual(expect, x)

    def test_Int(self):
        expect = [0, 2, 4, 6, 8]
        x = main.Array([8, 0, 2, 4, 6]).bubbleSort()
        self.assertEqual(expect, x)

    def test_Different_types(self):
        with self.assertRaises(TypeError):
            x = main.Array(["m", 1, "b", 4, 9]).bubbleSort()
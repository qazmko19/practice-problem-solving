from unittest import TestCase

from task import simple_array_sum


class SimpleArraySumTest(TestCase):
    def test_function1(self):
        array = [1, 2, 3, 4, 10, 11]
        self.assertEqual(31, simple_array_sum(array))

    def test_function2(self):
        array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(21, simple_array_sum(array))

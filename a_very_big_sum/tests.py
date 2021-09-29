from unittest import TestCase

from a_very_big_sum.task import a_very_big_sum


class AVeryBigSumTest(TestCase):
    def test_function1(self):
        array = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
        self.assertEqual(5000000015, a_very_big_sum(array))

    def test_function2(self):
        array = [162547823, 342135, 32951325897, 204387, 49204823094]
        self.assertEqual(82319243336, a_very_big_sum(array))

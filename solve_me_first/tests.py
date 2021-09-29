from unittest import TestCase
from unittest.mock import patch, MagicMock

from task import solve_me_first


class SolveMeFirstTest(TestCase):
    def test_function_1(self):
        self.assertEqual(solve_me_first(2, 3), 5)

    def test_function_2(self):
        self.assertEqual(solve_me_first(4, 6), 10)

    @patch('task.solve_me_first', return_value=10)
    def test_example_of_mocking(self, mocked_function: MagicMock):
        print(mocked_function.call_count)
        self.assertEqual(mocked_function(4, 6), 10)
        print(mocked_function.call_count)

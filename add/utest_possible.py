import unittest

import is_transformation_possible_function


class IsTransformationPossibleFunctionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            is_transformation_possible_function.is_transformation_possible('abcdef', [['fer', 'x'], ['a', 'h']], 1),
            True)

    def test_2(self):
        self.assertEqual(is_transformation_possible_function.is_transformation_possible('qwerty', [['*', 'w']], 0),
                         True)

    def test_3(self):
        self.assertEqual(is_transformation_possible_function.is_transformation_possible('xyz',
                                                                                        [['sa', '17'], ['yx', '43'],
                                                                                         ['xy', '@']], 2), True)

    def test_4(self):
        self.assertEqual(is_transformation_possible_function.is_transformation_possible('', [[' ', '17'], ['yx', 'xw'],
                                                                                             ['sazx', 'pfe4']], 1),
                         False)

    def test_5(self):
        self.assertEqual(
            is_transformation_possible_function.is_transformation_possible('qwerty', [['23', 'hf'], ['qweR', 'tr']], 1),
            False)


if __name__ == '__main__':
    unittest.main()

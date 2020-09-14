import unittest

import is_transformation_final_function


class IsTransformationFinalFunctionTest(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(is_transformation_final_function.is_transformation_final([['q', './']], 0), True)

    def test_2(self):
        self.assertAlmostEqual(
            is_transformation_final_function.is_transformation_final([['oir', 'dert'], ['pep', '..']], 1), True)

    def test_3(self):
        self.assertAlmostEqual(
            is_transformation_final_function.is_transformation_final([['*', 'dt'], ['zax', '.*'], ['qwe', 'we']], 2),
            False)

    def test_4(self):
        self.assertAlmostEqual(is_transformation_final_function.is_transformation_final([['*', '.*']], 0), True)

    def test_5(self):
        self.assertAlmostEqual(
            is_transformation_final_function.is_transformation_final([['qwe', 'ewq'], ['hgf', 'u..']], 1), False)

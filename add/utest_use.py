import unittest

import transformation_use_function


class TransformationUseFunctionTest(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('qwerty', [['q', 'w'], ['aqw', 'rew']], 0), 'wwerty')

    def test_2(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('abcdef', [['cde', 'w'], ['abcde', 'u']], 1), 'uf')

    def test_3(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('dadaya', [['*', 'az'], ['fder', '654']], 0), 'azdadaya')

    def test_4(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('dude', [['rew', 'pip'], ['*', 'suh'], ['dwkd', '2wm5']], 1),
            'suhdude')

    def test_5(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('dadaya', [['dad', '*'], ['fder', '654']], 0), 'aya')

    def test_6(self):
        self.assertAlmostEqual(transformation_use_function.transformation_use('dew', [['dew', '*']], 0), '')

    def test_7(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('dew', [['saqwe', 'porew'], ['dew', 'mountain'], ['*', '*']],
                                                           2), 'dew')

    def test_8(self):
        self.assertAlmostEqual(
            transformation_use_function.transformation_use('haha', [['qwe', 'pfer'], ['*', '*'], ['sax', 'ofon']], 1),
            'haha')


if __name__ == '__main__':
    unittest.main()

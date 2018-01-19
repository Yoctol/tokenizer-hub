from unittest import TestCase

from .. import NltkCustomJiebaTokenizer


class NltkCustomJiebaTokenizerTestCase(TestCase):

    def setUp(self):
        self.tokenizer = NltkCustomJiebaTokenizer()

    def test_lcut(self):
        test_cases = [
            ('我想喝珍珠奶茶半糖大杯',
             ['我', '想', '喝', '珍珠奶茶', '半糖', '大杯']),
            ('i would like to drink pearl milk tea.',
             ['i', 'would', 'like', 'to', 'drink', 'pearl', 'milk', 'tea', '.']),
            ('_ya_ 我想喝 _num_ 杯 _test_ 飲料 _end_',
             ['_ya_', '我', '想', '喝', '_num_', '杯', '_test_', '飲料', '_end_']),
            ('我想買12張(abc)股',
             ['我', '想', '買', '12', '張', '(', 'abc', ')', '股']),
            ('我想買 12 張 abc 股', ['我', '想', '買', '12', '張', 'abc', '股']),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    self.tokenizer.lcut(sentence=test_case[0]),
                )

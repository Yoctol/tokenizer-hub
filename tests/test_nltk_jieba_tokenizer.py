from unittest import TestCase

from .. import NltkJiebaTokenizer


class NltkJiebaTokenizerTestCase(TestCase):

    def test_lcut(self):
        tokenizer = NltkJiebaTokenizer()
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
                    tokenizer.lcut(sentence=test_case[0]),
                )

    def test_lcut_punct_false(self):
        tokenizer = NltkJiebaTokenizer()
        self.assertEqual(
            ['How', "'s", 'it', 'going', 'today', ',', 'Mr.Smith', '?', ],
            tokenizer.lcut("How's it going today, Mr.Smith?", punct=False),
        )
        tokenizer = NltkJiebaTokenizer(punct=False)
        self.assertEqual(
            ['How', "'s", 'it', 'going', 'today', ',', 'Mr.Smith', '?', ],
            tokenizer.lcut("How's it going today, Mr.Smith?"),
        )

    def test_lcut_HMM_false(self):
        tokenizer = NltkJiebaTokenizer()
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯', HMM=False),
        )
        tokenizer = NltkJiebaTokenizer(HMM=False)
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯'),
        )

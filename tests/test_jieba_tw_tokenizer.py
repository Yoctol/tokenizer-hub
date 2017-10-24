from unittest import TestCase

from .. import JiebaTWTokenizer


class JiebaTWTokenizerTestCase(TestCase):

    def test_JiebaTWTokenizer_hmm(self):
        tokenizer = JiebaTWTokenizer()
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半糖', '大', '杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯'),
        )

    def test_JiebaTWTokenizer(self):
        tokenizer = JiebaTWTokenizer()
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯', False),
        )

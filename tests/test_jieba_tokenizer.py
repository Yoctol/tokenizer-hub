from unittest import TestCase

from .. import JiebaTokenizer


class JiebaTokenizerTestCase(TestCase):

    def test_JiebaTokenizer_hmm(self):
        tokenizer = JiebaTokenizer()
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半糖', '大杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯'),
        )

    def test_JiebaTokenizer(self):
        tokenizer = JiebaTokenizer()
        self.assertEqual(
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯', False),
        )

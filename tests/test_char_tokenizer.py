# -*- coding: utf-8 -*-
from unittest import TestCase

from .. import CharTokenizer


class CharTokenizerTestCase(TestCase):

    def setUp(self):
        self.tokenizer = CharTokenizer()

    def test_CharTokenizer(self):
        self.assertEqual(
            ['我', '想', '要', '買', 'miss', 'm', '的', '蛋', '糕'],
            self.tokenizer.lcut('我想要買miss.M的蛋糕'),
        )
        self.assertEqual(
            ['來', '一', '卡', '車', 'mm', 'chocolate'],
            self.tokenizer.lcut('來一卡車~#MM chocolate#~'),
        )
        self.assertEqual(
            ['想', '要', '買', 'b', '股'],
            self.tokenizer.lcut('想要買(B股)'),
        )
        self.assertEqual(
            ['來', '一', '杯', '40.77', '度', '的', 'pink', 'lady'],
            self.tokenizer.lcut('來一杯40.77度的pink lady'),
        )

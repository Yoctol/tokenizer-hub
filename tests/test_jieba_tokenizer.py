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
            tokenizer.lcut('我想喝珍珠奶茶半糖大杯', HMM=False),
        )

    def test_JiebaTokenizer_parallel(self):
        tokenizer = JiebaTokenizer()
        human_tokened_sentences = [
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            ['你', '想', '喝', '珍珠奶茶', '半', '糖', '小杯'],
            ['他', '想', '喝', '珍珠奶茶', '全', '糖', '大', '杯'],
            ['她', '想', '喝', '珍珠奶茶', '半', '糖', '大', '杯'],
            ['我', '想', '喝', '珍珠奶茶', '半', '糖', '中', '杯'],
        ]
        origin_sentences = [
            '我想喝珍珠奶茶半糖大杯',
            '你想喝珍珠奶茶半糖小杯',
            '他想喝珍珠奶茶全糖大杯',
            '她想喝珍珠奶茶半糖大杯',
            '我想喝珍珠奶茶半糖中杯',
        ]
        tokenized_sentences = tokenizer.lcut_sentences(
            origin_sentences,
            num_jobs=8,
            HMM=False,
        )
        self.assertListEqual(human_tokened_sentences, tokenized_sentences)

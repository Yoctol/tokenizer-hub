from unittest import TestCase

from .. import CustomJiebaTokenizer


class CustomJiebaTokenizerTestCase(TestCase):

    def setUp(self):
        self.tokenizer = CustomJiebaTokenizer()

    def test_lcut_with_extra_words(self):
        sentence = '我想吃珍珠奶茶鍋，加一道普羅旺斯主廚香煎烤雞排'
        extra_words = ['珍珠奶茶鍋', '普羅旺斯主廚香煎烤雞排']
        expected_tokens = ['我', '想', '吃', '珍珠奶茶鍋',
                           '，', '加', '一道', '普羅旺斯主廚香煎烤雞排']
        actual_tokens = self.tokenizer.lcut(sentence, extra_words=extra_words)
        self.assertEqual(expected_tokens, actual_tokens)

    def test_no_side_effects_after_lcut(self):
        sentence = '我想吃珍珠奶茶鍋，加一道普羅旺斯主廚香煎烤雞排'
        extra_words = ['珍珠奶茶鍋', '普羅旺斯主廚香煎烤雞排']
        old_result = self.tokenizer.lcut(sentence)
        self.tokenizer.lcut(sentence, extra_words=extra_words)
        new_result = self.tokenizer.lcut(sentence)
        self.assertEqual(old_result, new_result)

    def test_lcut_sentences(self):
        sentences = [
            '蔣勤彥不喜歡吃牛味很重的大塊牛肉麵',
            '建甫大大的貓貓帽子很厲害',
        ]
        actual_list_of_tokens = self.tokenizer.lcut_sentences(sentences)
        expected_list_of_tokens = [
            ['蔣勤彥', '不', '喜歡', '吃', '牛味', '很重', '的', '大塊', '牛肉', '麵'],
            ['建甫', '大大的', '貓貓', '帽子', '很', '厲害'],
        ]
        self.assertEqual(expected_list_of_tokens, actual_list_of_tokens)

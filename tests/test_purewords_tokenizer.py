from unittest import TestCase

from .. import PureWordsTokenizer


class PurewordsTokenizerTestCase(TestCase):

    def setUp(self):
        self.tokenizer = PureWordsTokenizer()

    def test_lcut(self):
        sentence = "薄餡=柏憲=cph=cph_is_god\n讚讚讚！聯絡方式：cph@cph.tw, 0912345678"
        answer = ['薄餡', '柏憲', 'cph', 'cph', 'is', 'god',
                  '讚', '讚', '讚', '聯絡', '方式', '_url_', '_phone_']
        result = self.tokenizer.lcut(sentence)
        self.assertEqual(answer, result)

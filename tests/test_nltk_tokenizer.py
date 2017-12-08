from unittest import TestCase
from .. import NltkTokenizer


class test_NltkTokenizer(TestCase):
    
    def test_NltkTokenizer(self):
        tokenizer = NltkTokenizer()
        self.assertEqual(
            ['how', "'s", 'it', 'going', 'today', ',', 'mr.smith', '?'],
            tokenizer.lcut("How's it going today, Mr.Smith?", punct=False)
        )
    
    def test_NltkTokenizer_punct(self):
        tokenizer = NltkTokenizer()
        self.assertEqual(
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mr', '.', 'smith', '?'],
            tokenizer.lcut("How's it going today, Mr.Smith?", punct=True)
        )
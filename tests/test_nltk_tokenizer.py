from unittest import TestCase

from .. import NltkTokenizer


class test_NltkTokenizer(TestCase):

    def test_NltkTokenizer(self):
        tokenizer = NltkTokenizer()
        self.assertEqual(
            ['how', "'s", 'it', 'going', 'today', ',', 'mr.smith', '?', ],
            tokenizer.lcut("How's it going today, Mr.Smith?", punct=False),
        )

    def test_NltkTokenizer_punct(self):
        tokenizer = NltkTokenizer()
        self.assertEqual(
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mr', '.', 'smith', '?', ],
            tokenizer.lcut("How's it going today, Mr.Smith?", punct=True),
        )

    def test_NltkTokenizer_parallel_lcut(self):
        tokenizer = NltkTokenizer()
        human_tokened_sentences = [
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mr', '.', 'smith', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mr', '.', 'john', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mrs', '.', 'watson', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mrs', '.', 'stone', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'dr', '.', 'smith', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'dr', '.', 'john', '?', ],
            ['how', "'", 's', 'it', 'going', 'today', ',', 'mrs', '.', 'winslet', '?', ],
        ]
        sentences_to_token = [
            "How's it going today, Mr.Smith?",
            "How's it going today, Mr.John?",
            "How's it going today, Mrs.Watson?",
            "How's it going today, Mrs.Stone?",
            "How's it going today, Dr.Smith?",
            "How's it going today, Dr.John?",
            "How's it going today, Mrs.Winslet?",
        ]
        tokenized_sentences = tokenizer.lcut_sentences(
            sentences_to_token,
            num_jobs=4,
            punct=True,
        )
        self.assertListEqual(human_tokened_sentences, tokenized_sentences)

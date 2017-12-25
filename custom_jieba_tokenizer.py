from typing import Dict, List

from .parallel_jieba_tokenizer import ParallelJiebaTokenizer, strdecode

from .base_tokenizer import BaseTokenizer


class CustomJiebaTokenizer(ParallelJiebaTokenizer, BaseTokenizer):

    def add_word_idempotent(
            self,
            word: str,
        ) -> Dict[str, int]:
        word = strdecode(word)
        freq = 1
        self.FREQ[word] = freq
        self.total += freq

        existed_token = {}
        for ch in range(len(word)):
            wfrag = word[:ch + 1]
            if wfrag not in self.FREQ:
                self.FREQ[wfrag] = 0
            else:
                existed_token[wfrag] = self.FREQ[wfrag]
        return existed_token

    def del_word_idempotent(
            self,
            word: str,
            existed_tokens: Dict[str, int],
        ) -> None:
        word = strdecode(word)
        self.total -= self.FREQ[word]
        del self.FREQ[word]

        for ch in range(len(word)):
            wfrag = word[:ch + 1]
            if wfrag not in existed_tokens and self.FREQ[wfrag] == 0:
                del self.FREQ[wfrag]

    def lcut(
            self,
            sentence: str,
            extra_words: List[str] = None,
        ) -> List[str]:
        self.check_initialized()
        if extra_words is None:
            extra_words = []

        existed_tokens = {}
        for word in extra_words:
            _existed_tokens = self.add_word_idempotent(word)
            existed_tokens = {**existed_tokens, **_existed_tokens}
        result = super().lcut(sentence, cut_all=False, HMM=True)
        for word in extra_words:
            self.del_word_idempotent(word, existed_tokens)
        return result

    def lcut_sentences(self, sentences, num_jobs=8, use_hmm=True):
        return super().lcut_senteces(sentences, num_jobs, use_hmm)

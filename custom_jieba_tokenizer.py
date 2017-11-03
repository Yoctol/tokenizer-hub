from jieba import Tokenizer, strdecode


class CustomJiebaTokenizer(Tokenizer):

    def add_word_idempotent(self, word):
        word = strdecode(word)
        # freq = self.suggest_freq(word, False)
        freq = 1
        self.FREQ[word] = freq
        self.total += freq

        for ch in range(len(word)):
            wfrag = word[:ch + 1]
            if wfrag not in self.FREQ:
                self.FREQ[wfrag] = 0

        # self.total = sum([v for v in self.FREQ.values()])

    def del_word_idempotent(self, word):
        word = strdecode(word)
        self.total -= self.FREQ[word]
        del self.FREQ[word]

        for ch in range(len(word)):
            wfrag = word[:ch + 1]
            if wfrag in self.FREQ and self.FREQ[wfrag] == 0:
                del self.FREQ[wfrag]

    def lcut_with_extra_words(self, sentence, extra_words):
        for word in extra_words:
            self.add_word_idempotent(word)
        result = self.lcut(sentence, cut_all=False, HMM=True)
        for word in extra_words:
            self.del_word_idempotent(word)
        return result

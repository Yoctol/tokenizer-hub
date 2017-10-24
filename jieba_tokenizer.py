from jieba import Tokenizer


class JiebaTokenizer(object):

    def __init__(self, dict_path=None, freq_words=None):
        self.tokenizer = Tokenizer()
        if dict_path is not None:
            self.tokenizer.load_userdict(dict_path)
        if freq_words is not None:
            for f_word in freq_words:
                self.tokenizer.suggest_freq(f_word, True)

    def lcut(self, sentence, use_hmm=True):
        return self.tokenizer.lcut(sentence, HMM=use_hmm)

    def cut(self, sentence, use_hmm=True):
        return self.tokenizer.cut(sentence, HMM=use_hmm)

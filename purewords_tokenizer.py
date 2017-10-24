import purewords


class PureWordsTokenizer(object):

    def lcut(self, sentence):
        return purewords.clean_sentence(sentence).split(' ')

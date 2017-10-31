import purewords


class PureWordsTokenizer(object):

    def lcut(self, sentence):
        clean_sentence = purewords.clean_sentence(sentence)
        if clean_sentence == '':
            return []
        else:
            return clean_sentence.split(' ')

import nltk
nltk.download('punkt')  # noqa
from nltk.tokenize import WordPunctTokenizer, word_tokenize

from .base_tokenizer import BaseTokenizer


class NltkTokenizer(BaseTokenizer):

    def __init__(
            self,
        ):
        self.WPtokenizer = WordPunctTokenizer()

    def lcut(
            self,
            sentence,
            punct=True,
        ):
        sentence = sentence.lower()
        if punct is True:
            return(self.WPtokenizer.tokenize(sentence))
        else:
            return(word_tokenize(sentence))

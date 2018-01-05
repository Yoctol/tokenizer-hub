from typing import List
import nltk
nltk.download('punkt')  # noqa
import functools
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
            **kwargs
        ):
        if punct is True:
            return(self.WPtokenizer.tokenize(sentence))
        else:
            return(word_tokenize(sentence))

    def lcut_sentences(
            self,
            sentences: List[str],
            num_jobs: int = 8,
            punct: bool = True,
        ) -> List[List[str]]:

        from multiprocessing import cpu_count, Pool
        if num_jobs is None:
            num_jobs = cpu_count()
        with Pool(num_jobs) as pool:
            results = pool.map(
                functools.partial(
                    self.lcut,
                    punct=punct,
                ),
                sentences,
            )
        return results

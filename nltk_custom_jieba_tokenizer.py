from typing import List
import string

import re
import functools

from .base_tokenizer import BaseTokenizer
from .nltk_tokenizer import NltkTokenizer
from .custom_jieba_tokenizer import CustomJiebaTokenizer


class NltkCustomJiebaTokenizer(BaseTokenizer):

    def __init__(
            self,
            punct: bool = None,
            cut_all: bool = None,
            HMM: bool = None,
        ):
        self.nltk_tokenizer = NltkTokenizer()
        self.custom_jieba_tokenizer = CustomJiebaTokenizer()
        self.prog = re.compile('[{}]+'.format(string.printable))
        self.punct = punct
        self.cut_all = cut_all
        self.HMM = HMM

    def lcut(
            self,
            sentence: str,
            punct: bool = True,
            extra_words: List[str] = None,
            cut_all: bool = False,
            HMM: bool = True,
            num_jobs: int = 4,
            **kwargs  # noqa
        ) -> List[str]:
        if self.punct is not None:
            punct = self.punct
        if self.cut_all is not None:
            cut_all = self.cut_all
        if self.HMM is not None:
            HMM = self.HMM
        tokens = self.nltk_tokenizer.lcut(
            sentence=sentence,
            punct=punct,
        )
        output_tokens = []
        for token in tokens:
            eng_num = self.prog.sub('', token)
            if len(eng_num) > 0:
                output_tokens.append(
                    self.custom_jieba_tokenizer.lcut(
                        sentence=token,
                        extra_words=extra_words,
                        cut_all=cut_all,
                        HMM=HMM,
                    ),
                )
            else:
                output_tokens.append([token])
        return sum(output_tokens, [])

    def lcut_sentences(
            self,
            sentences: List[str],
            punct: bool = True,
            extra_words: List[str] = None,
            cut_all: bool = False,
            HMM: bool = True,
            num_jobs: int = None,
        ) -> List[List[str]]:
        from multiprocessing import cpu_count, Pool
        if num_jobs is None:
            num_jobs = cpu_count()
        if self.punct is not None:
            punct = self.punct
        if self.cut_all is not None:
            cut_all = self.cut_all
        if self.HMM is not None:
            HMM = self.HMM
        with Pool(num_jobs) as pool:
            results = pool.map(
                functools.partial(
                    self.lcut,
                    punct=punct,
                    extra_words=extra_words,
                    cut_all=cut_all,
                    HMM=HMM,
                    num_jobs=1,
                ),
                sentences,
            )
        return results

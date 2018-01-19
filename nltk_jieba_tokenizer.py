from typing import List
import string

import re
import functools

from .base_tokenizer import BaseTokenizer
from .nltk_tokenizer import NltkTokenizer
from .jieba_tokenizer import JiebaTokenizer


class NltkJiebaTokenizer(BaseTokenizer):

    def __init__(
            self,
            dict_path: str = None,
            freq_words: List[str] = None,
        ):
        self.nltk_tokenizer = NltkTokenizer()
        self.jieba_tokenizer = JiebaTokenizer(
            dict_path=dict_path,
            freq_words=freq_words,
        )
        self.prog = re.compile('[{}]+'.format(string.printable))

    def lcut(
            self,
            sentence: str,
            punct: bool = True,
            cut_all: bool = False,
            HMM: bool = True,
            num_jobs: int = 4,
            **kwargs  # noqa
        ) -> List[str]:
        tokens = self.nltk_tokenizer.lcut(
            sentence=sentence,
            punct=punct,
        )
        output_tokens = []
        for token in tokens:
            eng_num = self.prog.sub('', token)
            if len(eng_num) > 0:
                output_tokens.append(
                    self.jieba_tokenizer.lcut(
                        sentence=token,
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
            cut_all: bool = False,
            HMM: bool = True,
            num_jobs: int = None,
        ) -> List[List[str]]:
        from multiprocessing import cpu_count, Pool
        if num_jobs is None:
            num_jobs = cpu_count()
        with Pool(num_jobs) as pool:
            results = pool.map(
                functools.partial(
                    self.lcut,
                    punct=punct,
                    cut_all=cut_all,
                    HMM=HMM,
                    num_jobs=1,
                ),
                sentences,
            )
        return results

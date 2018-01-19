from typing import List

from .parallel_jieba_tokenizer import ParallelJiebaTokenizer
from .base_tokenizer import BaseTokenizer
import functools


class JiebaTokenizer(BaseTokenizer):

    def __init__(
            self,
            dict_path: str = None,
            freq_words: List[str] = None,
        ):
        self.tokenizer = ParallelJiebaTokenizer()
        if dict_path is not None:
            self.tokenizer.load_userdict(dict_path)
        if freq_words is not None:
            for f_word in freq_words:
                self.tokenizer.suggest_freq(f_word, True)

    def lcut(
            self,
            sentence: str,
            cut_all: bool = False,
            HMM: bool = True,
            **kwargs  # noqa
        ) -> List[str]:
        return self.tokenizer.lcut(
            sentence,
            cut_all=cut_all,
            HMM=HMM,
        )

    def lcut_sentences(
            self,
            sentences: List[str],
            num_jobs: int = 8,
            cut_all: bool = False,
            HMM: bool = True,
        ) -> List[List[str]]:
        from multiprocessing import cpu_count, Pool
        if num_jobs is None:
            num_jobs = cpu_count
        with Pool(num_jobs) as pool:
            results = pool.map(
                functools.partial(
                    self.tokenizer.lcut,
                    cut_all=cut_all,
                    HMM=HMM,
                ),
                sentences,
            )
        return results

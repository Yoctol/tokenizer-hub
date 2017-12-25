from typing import List

import purewords

from .base_tokenizer import BaseTokenizer


class PureWordsTokenizer(BaseTokenizer):

    def lcut(
            self,
            sentence: str,
        ) -> List[str]:
        clean_sentence = purewords.clean_sentence(sentence)
        if clean_sentence == '':
            return []
        else:
            return clean_sentence.split(' ')

    def lcut_sentences(
            self,
            sentences: List[str],
            num_jobs: int = 8,
        ) -> List[List[str]]:
        from multiprocessing import cpu_count, Pool
        if num_jobs is None:
            num_jobs = cpu_count()
        with Pool(num_jobs) as pool:
            tokenized_sentences = pool.map(self.lcut, sentences)
        return tokenized_sentences

from typing import List

from .ParallelJiebaTokenizer import ParallelJiebaTokenizer

from .base_tokenizer import BaseTokenizer


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
            use_hmm: bool = True,
        ) -> List[str]:
        return self.tokenizer.lcut(sentence, HMM=use_hmm)

    def lcut_sentences(
            self,
            sentences: List[str],
            num_jobs: int = 8,
            use_hmm: bool = True,
        ) -> List(str):
        return self.tokenizer.lcut_sentences(sentences, num_jobs, use_hmm)

    def cut(
            self,
            sentence: str,
            use_hmm: bool = True,
        ) -> str:
        return self.tokenizer.cut(sentence, HMM=use_hmm)

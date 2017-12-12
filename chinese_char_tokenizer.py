from typing import List
import re

import purewords

from .base_tokenizer import BaseTokenizer


class ChineseCharTokenizer(BaseTokenizer):

    def __init__(self):
        self.prog = re.compile(
            "[0-9a-zA-Z\-\.\(\)\{\}\[\]#@!~,\<\>\+\=\*\^\|\?\_\^%\$:;]+",
        )
        self.whitespace_prog = re.compile("\s+")

    def lcut(
            self,
            sentence: str,
        ):
        records = self.prog.findall(sentence)
        sentence = self.whitespace_prog.sub(" ", sentence)
        sub_sentence = self.prog.sub("X", sentence)
        segment_list = sub_sentence.split(' ')
        tokenized_sentence = []
        for segment in segment_list:
            tokenized_sentence.append(list(segment))
        tokenized_sentence = sum(tokenized_sentence, [])
        r_idx = 0
        for idx, token in enumerate(tokenized_sentence):
            if token == "X":
                tokenized_sentence[idx] = records[r_idx]
                r_idx += 1
        return tokenized_sentence

    def cut(
            self,
            sentence: str,
        ):
        result = self.lcut(sentence)
        for char in result:
            yield char


class PureChineseCharTokenizer(BaseTokenizer):

    def __init__(self):
        self.purechartokenizer = purewords.PureWords(
            tokenizer=ChineseCharTokenizer(),
        )

    def lcut(
            self,
            sentence: str,
        ) -> List[str]:
        return self.purechartokenizer.clean_sentence(sentence).split(" ")

    def cut(
            self,
            sentence: str,
        ) -> str:
        result = self.lcut(sentence=sentence)
        for char in result:
            yield char

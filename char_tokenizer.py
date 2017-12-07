from typing import List
import re

import purewords

from .base_tokenizer import BaseTokenizer


def char_tokenize(sentence: str):
    if not isinstance(sentence, str):
        raise TypeError(
            'input sentence should be a string, now is {}'.format(type(sentence)))
    sentence = (sentence.strip()).lower()

    clean_sentence = re.sub(
        r'[\^\$\*\+\?\(\)\{\}\[\]\|\-,~!;/#@<>""]+', ' ', sentence)
    eng_words = re.findall(r'[a-zA-Z]+', clean_sentence)
    clean_sentence = re.sub(r'[a-zA-Z]+', 'X', clean_sentence)

    nums = re.findall(r'[0-9]+[\.]*[0-9]+', clean_sentence)
    clean_sentence = re.sub(r'[0-9]+[\.]*[0-9]+', 'N', clean_sentence)

    clean_sentence = re.sub(r'[ \.]+', '', clean_sentence)

    tokenized_sentence = (' '.join(clean_sentence)).split(' ')

    e_idx = n_idx = 0
    for idx, token in enumerate(tokenized_sentence):
        if token == 'X':
            tokenized_sentence[idx] = eng_words[e_idx]
            e_idx += 1
        elif token == 'N':
            tokenized_sentence[idx] = nums[n_idx]
            n_idx += 1

    return tokenized_sentence


class CharTokenizer(BaseTokenizer):

    @classmethod
    def lcut(
            cls,
            sentence: str,
        ):
        return char_tokenize(sentence)

    @classmethod
    def cut(
            cls,
            sentence: str,
        ):
        result = char_tokenize(sentence)
        for char in result:
            yield char


class PureCharTokenizer(BaseTokenizer):

    def __init__(self):
        self.purechartokenizer = purewords.PureWords(
            tokenizer=CharTokenizer(),
        )

    def lcut(
            self,
            sentence: List[str],
        ):
        return self.purechartokenizer.clean_sentence(sentence).split(' ')

    def cut(
            self,
            sentence: str,
        ):
        result = self.lcut(sentence=sentence)
        for char in result:
            yield char

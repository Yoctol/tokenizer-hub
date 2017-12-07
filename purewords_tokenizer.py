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

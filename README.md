# tokenizer-hub

[![CircleCI][circleci-image]][circleci-url]
[![pypi][pypi-image]][pypi-url]

[circleci-image]: https://circleci.com/gh/Yoctol/tokenizer-hub.svg?style=shield&circle-token=d0ccb90bd2548853a41b37c88d210c73ec4fa220
[circleci-url]: https://circleci.com/gh/Yoctol/tokenizer-hub
[pypi-image]: https://img.shields.io/pypi/v/tokenizer-hub.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/tokenizer-hub


yoctol 乂卍oO煞氣ㄟtokenizerOo卍乂

Tokenizers have the same interface of Jieba:

```python
from tokenizer_hub import XXX_tokenizer
tokenizer = XXX_tokenizer()
tokenizer.lcut('我来到北京清华大学')
> ['我', '来到', '北京', '清华大学']
```

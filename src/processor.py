from typing import List

from nltk import sent_tokenize


def process(text: str) -> List[str]:
    return sent_tokenize(text)
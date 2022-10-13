from typing import List

from nltk import sent_tokenize


def process(text: str) -> List[str]:
    try:
        return sent_tokenize(text)
    except:
        import nltk
        nltk.download('punkt')
        return sent_tokenize(text)
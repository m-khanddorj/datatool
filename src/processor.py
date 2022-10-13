from msilib.schema import Error
from typing import List

from nltk import sent_tokenize


def process(text: str) -> List[str]:
    try:
        return sent_tokenize(text)
    except Error as e:

        import nltk
        nltk.download('punkt')
        return sent_tokenize(text)
import re
from classPorter import Porter


def sentence_tokenizer(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        sentence_tokens = re.split("[.?!]", text)
    return sentence_tokens


def word_tokenizer(text):
    po = Porter()
    words = []
    tokens = text.split()
    for i in tokens:
        token = {
            'word': i,
            'pos': po.get_pos(i)
        }
        words.append(token)

    return words


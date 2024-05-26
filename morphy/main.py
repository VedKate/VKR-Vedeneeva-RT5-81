import prepocessing as pre
from sintaxAnalize import morphy_from_sentence



if __name__ == '__main__':
    s = 'меня'
    sent = pre.word_tokenizer(s)
    morphy_from_sentence(sent)


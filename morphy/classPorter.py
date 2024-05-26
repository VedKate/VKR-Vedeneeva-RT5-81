# -*- coding: utf-8 -*-

# PERFECTIVEGROUND - деепричастия совершенного вида (от гл сов. вида) (уехав, сказавши)
# REFLEXIVE - возвратный суффикс
# VERB - глагольные постфиксы
# NOUN - именные постфиксы
# DERIVATIONAL - именной суффикс для образования абстрактного существительного (DER туда же)
# SUPERLATIVE - превосходная форма прилагательных и причастий
import pymorphy2
import re


class Porter:

    def __init__(self, w):
        self.word = w

    def __init__(self):
        self.word = ''

    # дописать блок про наречия
    PRONOUN = re.compile("(я|ты|она|она|оно|они|мы|вы)$")
    PERFECTIVEGROUND = re.compile("(ив|ивши|ившись|ыв|ывши|ывшись)|(л?!((?<=[ая])(сь|в|вши|вшись)))$")
    REFLEXIVE = re.compile("(с[яь])$")
    ADJECTIVE = re.compile("(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$")
    PARTICIPLE = re.compile("((ивш|ывш|ующ)|((?<=[ая])(ем|нн|вш|ющ|щ)))$")
    VERB = re.compile(
        "((ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ут|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)|((?<=[ая])(ла|на|ете|йте|ли|й|л|ем|н|ло|но|ет|ют|ны|ть|ешь|нно)))$")
    NOUN = re.compile(
        "(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$")
    RVRE = re.compile("^(.*?[аеиоуыэюя])(.*)$")
    DERIVATIONAL = re.compile(".*[^аеиоуыэюя]+[аеиоуыэюя].*ость?$")
    DER = re.compile("ость?$")
    ma = pymorphy2.MorphAnalyzer()
    SUPERLATIVE = re.compile("(ейше|ейш)$")
    I = re.compile("и$")
    P = re.compile("ь$")
    NN = re.compile("нн$")
    partofspeech = "undef"

    def is_pronoun(self):
        word = self.word.lower()
        word = self.word.replace('ё', 'е')
        m = re.match(Porter.PRONOUN, word)

        if m is None:
            return False
        else:
            self.partofspeech = "PRONOUN"
            return True

    @staticmethod
    def stem(self):
        morphems = []
        word = self.word.lower()
        word = word.replace('ё', 'е')
        m = re.match(Porter.RVRE, word)
        if m and m.groups():
            pre = m.group(1)
            rv = m.group(2)
            temp = Porter.PERFECTIVEGROUND.sub('', rv, 1)
            if temp == rv:  # не деепричастие
                rv = Porter.REFLEXIVE.sub('', rv, 1)  # отсекаем возвратную частицу (от глаола)
                temp = Porter.ADJECTIVE.sub('', rv, 1)  # отсекаем окончание пригалательного от глагола
                if temp != rv:  # получили прилагетельное
                    rv = temp
                    rv = Porter.PARTICIPLE.sub('', rv, 1)  # причастие (тоже прилагательное)
                    Porter.partofspeech = "ADJECTIVE"
                else:
                    temp = Porter.VERB.sub('', rv, 1)
                    if temp == rv:
                        rv = Porter.NOUN.sub('', rv, 1)
                        Porter.partofspeech = "NOUN"
                    else:
                        rv = temp
                        Porter.partofspeech = "VERB"
            else:
                rv = temp
                Porter.partofspeech = "PERFECTIVEGROUND"

            rv = Porter.I.sub('', rv, 1)

            if re.match(Porter.DERIVATIONAL, rv):
                rv = Porter.DER.sub('', rv, 1)

            temp = Porter.P.sub('', rv, 1)
            if temp == rv:
                rv = Porter.SUPERLATIVE.sub('', rv, 1)
                rv = Porter.NN.sub('н', rv, 1)
            else:
                rv = temp
                Porter.partofspeech = "NOUN"
            word = pre + rv

        return word

    def get_part_of_speech(self):

        return self.partofspeech

    def get_pos(self, w):
        adj = ['ADJF', 'ADJS']
        verbs = ['VERB', 'INFN']
        others = ['NOUN', 'NPRO', 'PREP', 'CONJ', 'PRCL']

        if w == ',':
            return 'comma'

        report = self.ma.parse(w)[0]

        p = report.tag.POS
        if p in adj:
            return 'ADJECTIVE'
        elif p in verbs:
            return 'VERB'
        elif p in others:
            return p

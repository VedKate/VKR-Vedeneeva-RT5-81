import re
import pymorphy2.analyzer


class Verb:
    isinfinitive = 'undef'
    transitivity = 'undef'  # 'tran',переходный 'intr', непереходный
    reflexivity = 'undef'  # 'reflect', 'unreflect'
    aspect = 'undef'  # 'perf' совершенный вид  'impf'  несовершенный вид

    number = 'undef'
    tense = 'undef'  # 'pres' настоящее время, 'past' прошедшее время, 'futr' будущее время
    persons = 'undef'
    gender = 'undef'  # есть у ПРОШЕДШЕГО времени ЕДИНСВЕННОГО числа

    PREFIX = re.compile("(об|вы|вз|до|за|от|по|пере|под|при|про|у|раз|рас|)|(c)")

    PRESENTSING = re.compile("([ую])$|(ешь|ишь)$|(ет|ит)$")
    PRESENTPLUR = re.compile("(ем|им)$|(ете|ите)$|(ут|ют|ят)$")
    PAST = re.compile("(л$)|(ла$)|(ло$)|(ли$)")

    morph = pymorphy2.MorphAnalyzer()
    morphemes = []
    hypotheses = []

    def find_tags(self, word):
        m = re.search("(ся)$|(сь)$", word)  # возвраность

        if m is not None:
            g = m.lastindex
            self.reflexivity = 'reflect'
            self.morphemes.append(word[m.start(g):])
            word = word[:m.start(g)]  # ПЕРЕЗАПИСЬ
        else:
            self.reflexivity = 'unreflect'

        p = self.morph.parse(word)[0]  # переходность и вид
        self.aspect = p.tag.aspect
        self.transitivity = p.tag.transitivity

        # Непостоянные признаки
        m = re.sub("(ть|ти)$", '', word)  # ПЕРЕЗАПИСЬ

        if word != m:
            self.isinfinitive = 'true'
            self.push_tags(word)
            self.throw_tags() # закончили1
        else:
            self.isinfinitive = 'false'
            self.find_form_properties(word)

    def find_form_properties(self, word):
        genders = ['masc', 'femn', 'neut']
        perslist = ['1per', '2per', '3per']
        m = re.search(self.PAST, word)
        if m is not None:
            i = m.lastindex
            if i != 4:
                print(i)
                self.tense = 'past'
                self.number = 'sing'
                self.gender = genders[i - 1]
                for i in perslist:
                    self.persons = i
                    self.push_tags(word)


            elif i == 4:
                self.tense = 'past'
                self.number = 'plur'
                self.persons = 'undef'
            self.push_tags(word)
            self.throw_tags()  # закончили если мн.

        else:
            if self.aspect == 'perf':
                self.tense = 'futr'
            else:
                self.tense = 'pres'

            m = re.search(self.PRESENTSING, word)
            if m is not None:
                self.number = 'sing'
                self.persons = str(m.lastindex)+'per'
                self.push_tags(word)
            elif re.search(self.PRESENTPLUR, word) is not None:
                self.number = 'plur'
                self.persons = str(re.search(self.PRESENTPLUR, word).lastindex)+'per'
                self.push_tags(word)
            self.throw_tags()

    def push_tags(self, word):
        hypo = {'word': word,
                'isinfinitive': self.isinfinitive,
                'transitivity': self.transitivity,
                'reflexivity': self.reflexivity,
                'aspect': self.aspect,
                'number': self.number,
                'tense': self.tense,
                'persons': self.persons,
                'gender': self.gender
                }
        self.hypotheses.append(hypo)

    def get_tags(self):
        h = self.hypotheses
        self.hypotheses = []
        return h

    def throw_tags(self):
        self.isinfinitive = 'undef'
        self.transitivity = 'undef'
        self.reflexivity = 'undef'
        self.aspect = 'undef'

        self.number = 'undef'
        self.tense = 'undef'
        self.persons = 'undef'
        self.gender = 'undef'

    def morphy(self, word):
        self.find_tags(word)
        return self.get_tags()
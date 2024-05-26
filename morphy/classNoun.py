import re
import pymorphy2.analyzer


class Noun:
    cases = ["loct", "abit", "datv", "gent", "accs", "nomn"]  # пред, тв, дат, ро, вин, им
    PLUR = re.compile("(ах|ях)$|(ами|ями)$|(ам|ям)$|(ов|ев|ей)$|(ей)$|([ыияа])$")
    FIRSTDEC = re.compile("([ая])$|([ыи])$|(е)$|(у|[^ь]ю)$|(ой|ей|ою|ею)$")
    SECONDDEC = re.compile("([ое])$|([ая])$|(е)$|([ую])$|(ом|ем)$")
    THIRDDEC = re.compile("(и)$|(ью)$|(ь)$")
    gender = "undef"  #
    declension = "undef"
    number = "undef"  # sing plur
    animacy = "undef"
    caselist = []
    hypotheses = []

    morph = pymorphy2.MorphAnalyzer()

    def find_tags(self, word):  # определение числа, и падежа
        searchobj = re.search(self.PLUR, word)

        parslist = self.morph.parse(word)
        nums = self.get_numbers(parslist)
        p = parslist[0]

        self.animacy = p.tag.animacy

        if nums == 1 or nums == 0:  # единственное число
            self.number = 'sing'
            self.gender = p.tag.gender

            # ср 2е скл
            if self.gender == "neut":  # средний род, 2е склонение
                self.declension = 'second'
                searchobj1 = re.search(self.SECONDDEC, word)
                m = searchobj1.lastindex

                if m == 1:
                    self.caselist.append("nomn")
                    self.caselist.append("accs")
                elif m == 2:
                    self.caselist.append("gent")
                elif m == 3:
                    self.caselist.append("loct")  # ([ое])$|([ая])$|(е)$|([ую])$|(ом|ем)$
                elif m == 4:
                    self.caselist.append("datv")
                elif m == 5:
                    self.caselist.append("abit")
                self.push_tags(word)
            # 1e скл
            searchobj3 = re.search(self.FIRSTDEC, word)
            if (self.gender == 'femn' or self.gender == 'masc') and searchobj3 is not None: # 1е скл
                # ("([ая])$|([ыи])$|(е)$|([ую])$|(ой|ей|ою|ею)$")
                self.declension = 'first'
                m = searchobj3.lastindex
                if m == 1:
                    self.caselist.append('nomn')
                elif m == 2:
                    self.caselist.append("gent")
                elif m == 3:
                    self.caselist.append("datv")  # ([ое])$|([ая])$|(е)$|([ую])$|(ом|ем)$
                    self.caselist.append("loct")
                elif m == 4:
                    self.caselist.append("accs")
                elif m == 5:
                    self.caselist.append("abit")
                self.push_tags(word)
                pass

            # мужской 2е скл.
            elif self.gender == 'masc':
                self.declension = 'second'
                searchobj2 = re.search(self.SECONDDEC, word)
                if len(word) <= 3 or searchobj2 is None:
                    self.caselist.append("nomn")
                    self.caselist.append("accs")
                else:
                    m = searchobj2.lastindex
                    if m == 1 or m == 3:
                        self.caselist.append("loct")
                    elif m == 2:
                        self.caselist.append("gent")
                    elif m == 4:
                        self.caselist.append("datv")
                    elif m == 5:
                        self.caselist.append("abit")
                self.push_tags(word)

                pass

            elif self.gender == 'femn' and searchobj3 is None:
                searchobj4 = re.search(self.THIRDDEC, word)
                self.declension = 'third'
                m = searchobj4.lastindex  # ("(и)$|(ью)$|(ь)$")
                if m == 1:
                    self.caselist.append('gent')
                    self.caselist.append("datv")
                    self.caselist.append("loct")
                elif m == 2:
                    self.caselist.append("abit")
                elif m == 3:
                    self.caselist.append("nomn")
                    self.caselist.append("accs")
            self.push_tags(word)



        if nums == 2 or nums == 0:
            m = searchobj.lastindex
            self.number = "plur"
            if m == 1:
                self.caselist.append("loct")
            elif m == 2:
                self.caselist.append("abit")
            elif m == 3:
                self.caselist.append("datv")
            elif m == 4:
                self.caselist.append("gent")
            elif m == 5:
                self.caselist.append("accs")
                self.caselist.append("gent")
            elif m == 6:
                self.caselist.append("nomn")
                if self.animacy == 'inan':
                    self.caselist.append("accs")
            self.push_tags(word)

        self.gender = "undef"
        self.declension = "undef"
        self.number = "undef"
        self.animacy = "undef"

    def push_tags(self, word):

        for i in self.caselist:
            hypo = {'word': word,
                    'part_of_speech': 'NOUN',
                    'number': self.number,
                    'declension': self.declension,
                    'gender': self.gender,
                    'animacy': self.animacy,
                    'case': i}
            self.hypotheses.append(hypo)

        self.caselist = []

    def get_tags(self):
        h = self.hypotheses
        self.hypotheses = []

        return h

    def morphy(self, word):
        self.find_tags(word)
        return self.get_tags()


    def get_numbers(self, parslist):
        sin = 0
        pl = 0
        for i in parslist:
            if i.tag.number == 'sing':
                sin = 1
            if i.tag.number == 'plur':
                pl = 1
        if sin == 1 and pl == 1:
            return 0
        elif sin == 1:
            return 1
        else:
            return 2




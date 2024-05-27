# TO DO: закончить

personal_pronouns = [
    {"word": "я", "person": "1per", "number": "sing", "case": "nomn"},
    {"word": "меня", "person": "1per", "number": "sing", "case": "gent"},
    {"word": "мне", "person": "1per", "number": "sing", "case": "datv"},
    {"word": "меня", "person": "1per", "number": "sing", "case": "accs"},
    {"word": "мной", "person": "1per", "number": "sing", "case": "abit"},
    {"word": "обо_мне", "person": "1per", "number": "sing", "case": "loct"},

    {"word": "мы", "person": "1per", "number": "plur", "case": "nomn"},
    {"word": "нас", "person": "1per", "number": "plur", "case": "gent"},
    {"word": "нам", "person": "1per", "number": "plur", "case": "datv"},
    {"word": "нас", "person": "1per", "number": "plur", "case": "accs"},
    {"word": "нами", "person": "1per", "number": "plur", "case": "abit"},
    {"word": "о_нас", "person": "1per", "number": "plur", "case": "loct"},

    {"word": "ты", "person": "2per", "number": "sing", "case": "nomn"},
    {"word": "тебя", "person": "2per", "number": "sing", "case": "gent"},
    {"word": "тебе", "person": "2per", "number": "sing", "case": "datv"},
    {"word": "тебя", "person": "2per", "number": "sing", "case": "accs"},
    {"word": "тобой", "person": "2per", "number": "sing", "case": "abit"},
    {"word": "о_тебе", "person": "2per", "number": "sing", "case": "loct"},

    {"word": "вы", "person": "2per", "number": "plur", "case": "nomn"},
    {"word": "вас", "person": "2per", "number": "plur", "case": "gent"},
    {"word": "вам", "person": "2per", "number": "plur", "case": "datv"},
    {"word": "вас", "person": "2per", "number": "plur", "case": "accs"},
    {"word": "вами", "person": "2per", "number": "plur", "case": "abit"},
    {"word": "о_вас", "person": "2per", "number": "plur", "case": "loct"},

    {"word": "он", "person": "3per", "number": "sing", "case": "nomn", "gender": "masc"},
    {"word": "его", "person": "3per", "number": "sing", "case": "gent", "gender": "masc"},
    {"word": "ему", "person": "3per", "number": "sing", "case": "datv", "gender": "masc"},
    {"word": "его", "person": "3per", "number": "sing", "case": "accs", "gender": "masc"},
    {"word": "им", "person": "3per", "number": "sing", "case": "abit", "gender": "masc"},
    {"word": "о нем", "person": "3per", "number": "sing", "case": "loct", "gender": "masc"},

    {"word": "она", "person": "3per", "number": "sing", "case": "nomn", "gender": "femn"},
    {"word": "ее", "person": "3per", "number": "sing", "case": "gent", "gender": "femn"},
    {"word": "ей", "person": "3per", "number": "sing", "case": "datv", "gender": "femn"},
    {"word": "ее", "person": "3per", "number": "sing", "case": "accs", "gender": "femn"},
    {"word": "ей", "person": "3per", "number": "sing", "case": "abit", "gender": "femn"},
    {"word": "о_ней", "person": "3per", "number": "sing", "case": "loct", "gender": "femn"},

    {"word": "оно", "person": "3per", "number": "sing", "case": "nomn", "gender": "neut"},
    {"word": "его", "person": "3per", "number": "sing", "case": "gent", "gender": "neut"},
    {"word": "ему", "person": "3per", "number": "sing", "case": "datv", "gender": "neut"},
    {"word": "его", "person": "3per", "number": "sing", "case": "accs", "gender": "neut"},
    {"word": "им", "person": "3per", "number": "sing", "case": "abit", "gender": "neut"},
    {"word": "о_нем", "person": "3per", "number": "sing", "case": "loct", "gender": "neut"},

    {"word": "они", "person": "3per", "number": "sing", "case": "nomn"},
    {"word": "их", "person": "3per", "number": "sing", "case": "gent"},
    {"word": "им", "person": "3per", "number": "sing", "case": "datv"},
    {"word": "их", "person": "3per", "number": "sing", "case": "accs"},
    {"word": "ими", "person": "3per", "number": "sing", "case": "abit"},
    {"word": "о_них", "person": "3per", "number": "sing", "case": "loct"},

]


def get_pnoun(word):
    reslist = []

    for i in personal_pronouns:
        res = {}
        if i["word"] == word:
            res = {
                "word": word,
                'part_of_speech': 'NPRO',
                "person": i["person"],
                "number": i["number"],
                "case": i["case"],
                "gender": "undef"
                   }
            if "gender" in i.keys():
                res["gender"] = i["gender"]
            reslist.append(res)

    return reslist





import re


class Adjective:

    gender = 'undef'
    number = 'undef'
    case = 'undef'

    def __init__(self):
        self.hypotheses = []

    def find_tags(self, word):
        endings = {
            'masc_sing_nomn': '([ыи]й$)|((ив|оват|еват|к|чат|ист|б)$)',  # мужской род, единственное число, именительный падеж
            'masc_sing_accs': '([ое]го$)|([ыи]й$)',  # мужской род, единственное число, винительный падеж
            'masc_sing_gent': '[ое]го$',  # мужской род, единственное число, родительный падеж
            'masc_sing_datv': '[ое]му$',  # мужской род, единственное число, дательный падеж
            'masc_sing_abit': '[иы]м$',  # мужской род, единственное число, творительный падеж
            'masc_sing_loct': '[ое]м$',  # мужской род, единственное число, предложный падеж

            'femn_sing_nomn': '([ая]я$)|([ая]$)',  # женский род, единственное число, именительный падеж
            'femn_sing_accs': '[ую]ю$',  # женский род, единственное число, винительный падеж
            'femn_sing_gent': '[ео]й$',  # женский род, единственное число, родительный падеж
            'femn_sing_datv': '[ое]й$',  # женский род, единственное число, дательный падеж
            'femn_sing_abit': '[ео]й$',  # женский род, единственное число, творительный падеж
            'femn_sing_loct': '[ео]й$',  # женский род, единственное число, предложный падеж

            'neut_sing_nomn': '[ое]$',  # средний род, единственное число, именительный падеж
            'neut_sing_accs': '([ео]е$)|([ое]го$)',  # средний род, единственное число, винительный падеж
            'neut_sing_gent': '[ое]го$',  # средний род, единственное число, родительный падеж
            'neut_sing_datv': '[ое]му$',  # средний род, единственное число, дательный падеж
            'neut_sing_abit': '[ыи]м$',  # средний род, единственное число, творительный падеж
            'neut_sing_loct': '[ео]м$',  # средний род, единственное число, предложный падеж

            'undef_plur_nomn': '[ыи]е$',  # множественное число, именительный падеж
            'undef_plur_accs': '([ыи]х$)|([ыи]е$)',  # множественное число, винительный падеж
            'undef_plur_gent': '[ыи]х$',  # множественное число, родительный падеж
            'undef_plur_datv': '[ыи]м$',  # множественное число, дательный падеж
            'undef_plur_abit': '[ыи]ми$',  # множественное число, творительный падеж
            'undef_plur_loct': '[ыи]х$',  # множественное число, предложный падеж
        }

        for tag, pattern in endings.items():
            if re.search(pattern, word):
                gender, number, case = re.match(r'(.+?)_(.+?)_(.+)', tag).groups()
                self.gender = gender
                self.number = number
                self.case = case
                self.push_tags(word)

    def push_tags(self,wr):
        self.hypotheses.append({'word': wr,'part_of_speech': 'ADJF', 'gender': self.gender, 'number': self.number, 'case': self.case})

    def get_tags(self):
        h = self.hypotheses
        self.hypotheses = []
        return h

    def get_morphy(self, word):
        self.find_tags(word)
        return self.get_tags()

    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')
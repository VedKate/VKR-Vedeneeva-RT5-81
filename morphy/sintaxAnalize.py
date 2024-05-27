from classPorter import Porter
from classNoun import Noun
from classVedrb import Verb
from classAdjective import Adjective
from Pronoun import get_pnoun


def switch_from_pos(w):

    if w['pos'] == "NOUN":
        n = Noun()
        res = n.morphy(w['word'])
        del n
        return res
    elif w['pos'] == "VERB":
        return Verb().morphy(w['word'])
    elif w['pos'] == "NPRO":
        return get_pnoun(w['word'])
    if w['pos'] == "ADJECTIVE":
        return Adjective().get_morphy(w['word'])





def morphy_from_sentence(sent):
    properties = switch_from_pos(sent[0])
    print(sent, sent[0])

    return properties





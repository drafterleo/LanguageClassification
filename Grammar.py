from random import random, randint, choice
from NgVector import *


def choiceWayIdx(ways):
    # ways structure - [(2, 'X', 0.3), (3, 'V', 0.3), (4, 'R', 0.4)]
    max_p = 0.0
    way_idx = 0
    for i in range(len(ways)):
        p = random() + ways[i][2]
        if p > max_p:
            max_p = p
            way_idx = i
    return way_idx


def genWordByGrammar(grammar, maxLen = 10):
    node = 0
    word = ""
    while len(word) < maxLen:
        ways = grammar[node]
        if len(ways) == 0:
            break
        else:
            way_idx = choiceWayIdx(ways)
            node = ways[way_idx][0]
            word += ways[way_idx][1]
    return word


def genTextByGrammar(grammar, wordCount = 10):
    text = ""
    for i in range(wordCount):
        text += genWordByGrammar(grammar, randint(3, 15))
    return text


def checkGrammaticality(word, grammar) -> bool:
    node = 0
    result = True
    for ch in word:
        ways = grammar[node]
        has_way = False
        for way in ways:
            if way[1] == ch:
                node = way[0]
                has_way = True
                break
        if not has_way:
            result = False
            break
    return result


def genWordByProbabilityVector(ng_vect, word_len=10) -> str:
    res_word = ""
    for i in range(word_len):
        p = random()
        ch = choice(list(ng_vect))
        attempts = 1000
        while ng_vect[ch] < p and attempts > 0:
            ch = choice(list(ng_vect))
            attempts -= 1
        res_word += ch
    return res_word


grammar_1 = {0: [(1, 'X', 0.5), (2, 'V', 0.5)],
             1: [(1, 'M', 0.5), (3, 'X', 0.5)],
             2: [(2, 'T', 0.5), (4, 'V', 0.5)],
             3: [(2, 'R', 0.5), (5, 'M', 0.5)],
             4: [(3, 'T', 0.5), (5, 'X', 0.5)],
             5: []
             }

grammar_2 = {0: [(1, 'X', 0.3), (2, 'V', 0.7)],
             1: [(2, 'M', 0.5), (4, 'T', 0.5)],
             2: [(2, 'X', 0.3), (3, 'V', 0.3), (4, 'R', 0.4)],
             3: [(3, 'T', 0.5), (1, 'R', 0.5)],
             4: []
             }

def testGrammars():
    curr_grammar = grammar_1

    text = genTextByGrammar(curr_grammar, 2000)
    tst_vector = makeNgVector(text)

    print (text)
    printNgVector(tst_vector)
    # print len(tst_vector)
    normalizeNgVector(tst_vector)
    printNgVector(tst_vector)
    print ('-----------------------------------------------')

    texts = [genTextByGrammar(curr_grammar, 2000) for i in range(20)]

    avg_vector = makeAverageNgVector(texts)
    printNgVector(avg_vector)
    # print len(avg_vector)
    normalizeNgVector(avg_vector)
    printNgVector(avg_vector)


def testPtobabilityGenerator():
    curr_grammar = grammar_1
    text = genTextByGrammar(curr_grammar, 2000)
    tst_vector = makeNgVector(text, 1)
    normalizeNgVector(tst_vector)
    printNgVector(tst_vector)
    for i in range(10):
        prob_word = genWordByProbabilityVector(tst_vector, 3)
        gramm_word = genWordByGrammar(curr_grammar, 5)
        print(prob_word, checkGrammaticality(prob_word, curr_grammar),
              gramm_word, checkGrammaticality(gramm_word, curr_grammar))


testPtobabilityGenerator()


#testGrammars()
# w = genWordByGrammar(grammar_1)
# print(checkGrammaticality(w, grammar_1))
from math import sqrt, acos
from collections import OrderedDict


def makeNgVector(text: str, ngLen: int=3) -> dict:
    vect = {}
    for i in range(len(text) - ngLen):
        ng = text[i:ngLen + i]
        vect[ng] = vect.get(ng, 0) + 1
    return vect


def normalizeNgVector(ng_vect: dict):
    ng_sum = sum(ng_vect.values())
    for i in ng_vect.keys():
        ng_vect[i] /= ng_sum


def makeAverageNgVector(texts: list) -> dict:
    vect_sum = {}
    text_count = len(texts)
    for i in range(0, text_count):
        vect_i = makeNgVector(texts[i])
        for k in vect_i.keys():
            vect_sum[k] = vect_sum.get(k, 0) + vect_i[k]
    for i in vect_sum.keys():
        vect_sum[i] /= text_count
    return vect_sum


def printNgVector(ng_vect, comment=""):
    print (comment, OrderedDict(sorted(ng_vect.items(), key=lambda t: t[1], reverse=True)))


def compareNgVectorsByDistance(vect0, vect1: dict) -> float: # compare normalized vectors
    distance = 0.0
    for i in vect0.keys():
        d = vect0[i] - vect1.get(i, 0)
        distance += abs(d) # distance += d ** 2
    return distance # return sqrt(distance)


def compareNgVectorsByAngle(vect0, vect1: dict) -> float: # compare normalized vectors
    dot_prod = 0.0
    vect0_len = 0.0
    vect1_len = 0.0
    for i in vect0.keys():
        dot_prod += vect0[i] * vect1.get(i, 0)
        vect0_len += vect0[i] ** 2
        vect1_len += vect1.get(i, 0) ** 2
    if vect0_len > 0.0 and vect1_len > 0.0:
        return acos(dot_prod / sqrt(vect0_len * vect1_len))
    else:
        return float("inf")



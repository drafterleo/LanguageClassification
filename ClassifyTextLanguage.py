from NgVector import *
from random import choice
from unidecode import unidecode


def filterText(text: str, transliterate=True) -> str:
    if transliterate:
        f_str = unidecode(text)
    return "".join([ch for ch in f_str.lower() if ch.isalpha()]) #join(filter(str.isalpha, f_str.lower()))


def filterTxtFile(fileName: str, transliterate=True) -> str:
    f = open(fileName, "r", encoding="utf-8")
    f_str = f.read()
    f.close()
    return filterText(f_str, transliterate)


def genRandomTextFile(fileName: str, textLen=500):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    text = ""
    for i in range(textLen):
        text += choice(alphabet)
    f = open(fileName, "w", encoding="utf-8")
    f.write(text)
    f.close()


def makeNgVectorByText(text: str, normalize=True) -> str:
    vector = makeNgVector(text, 3)
    if normalize:
        normalizeNgVector(vector)
    return vector


def makeNgVectorByTextFile(fileName: str, normalize=True) -> str:
    text = filterTxtFile(fileName, transliterate=True)
    vector = makeNgVectorByText(text, normalize)
    # printNgVector(vector, fileName)
    return vector


def appendNgVectorToBase(textFile: str, langName: str, base: dict):
    base[langName] = makeNgVectorByTextFile(textFile)


def classifyTextByMinFn(text: str, base: dict, compareFn, comment="") -> str:
    tst_vector = makeNgVectorByText(text)
    min_d = float("inf") # infinity
    res_lang = ""
    for lang in base.keys():
        d = compareFn(tst_vector, base[lang])
        print (comment + lang + ":", d)
        if d < min_d:
            min_d = d
            res_lang = lang
    return res_lang


def classifyLanguage():
    lang_vectors= {} # {"lng": ng_vector, ...}

    #genRandomTextFile("text_rnd.txt", 100000)

    appendNgVectorToBase("text_rus.txt", langName="rus", base=lang_vectors)
    appendNgVectorToBase("text_ukr.txt", langName="ukr", base=lang_vectors)
    appendNgVectorToBase("text_bel.txt", langName="bel", base=lang_vectors)
    appendNgVectorToBase("text_blg.txt", langName="blg", base=lang_vectors)
    appendNgVectorToBase("text_eng.txt", langName="eng", base=lang_vectors)
    appendNgVectorToBase("text_jbo.txt", langName="jbo", base=lang_vectors)
    appendNgVectorToBase("text_epo.txt", langName="epo", base=lang_vectors)
    appendNgVectorToBase("text_pol.txt", langName="pol", base=lang_vectors)

    #appendVectorToBase("text_rnd.txt", "rnd", lang_vector_base)

    print("-------------------------------------------------------------")

    text = filterTxtFile("tst_rus.txt", transliterate=True)
    print(text, '\n')

    print(classifyTextByMinFn(text, lang_vectors, compareNgVectorsByDistance, "distance to "))
    print(classifyTextByMinFn(text, lang_vectors, compareNgVectorsByAngle, "angle with "))

    # rus_vector = makeNgVectorByTextFile("text_rus.txt", False)
    # print (rus_vector['och'])


if __name__ == "__main__":
    classifyLanguage()
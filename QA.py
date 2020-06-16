import re
from nltk.stem import PorterStemmer
import spacy

spacy_nlp = spacy.load('en_core_web_sm')

def findIntersection(lst1, lst2):
    ps = PorterStemmer()
    #print("lst1",lst1)
    #print("lst2",lst2)
    lst3 = [value for value in lst1 if ps.stem(value.lower()) in lst2]
    #print(lst3)
    return lst3


def findAnswer(f, question):
    # f = open("demo", "r").read()
    '''
    doc = spacy_nlp(f)
    tokens = [token.text for token in doc if not token.is_stop]
    s = ""
    for tok in tokens:
        s += tok + " "
    '''
    l = f.split(".")

    l = [i for i in l if i != '']

    # question = input("Enter the question.")
    ps = PorterStemmer()
    qdoc = spacy_nlp(question)
    qtok = [token.text for token in qdoc if not token.is_stop]
    ql = [ps.stem(i.lower()) for i in qtok]

    intersection = [len(findIntersection(i.split(), ql)) for i in l]

    # print(intersection)
    # for i in range(len(intersection)):
    #    print(i,intersection[i],l[i])
    # print(intersection.index(max(intersection)))
    # print(l[intersection.index(max(intersection))])
    return l[intersection.index(max(intersection))]
    # Who felt worried
    # Who enjoyed looking at the tall trees and lovely flowers
    # Apart from tall trees what did he enjoy
'''
f = input("Passage:")
a = input("que")
psg = "Walton was a lawer. He had 3 daughters. His Daughter was a Doctor."
que = "who was doctor ?"
print(findAnswer(psg,que))
'''
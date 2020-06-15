import re
from nltk.stem import PorterStemmer


def findIntersection(lst1, lst2):
    ps = PorterStemmer()
    lst3 = [ps.stem(value.lower()) for value in lst1 if value in lst2]
    # print(lst3)
    return lst3


def findAnswer(f, question):
    # f = open("demo", "r").read()
    s = ''.join(f.split("\n"))
    s = re.sub("[!?\"]", " ", s)

    l = s.split(".")

    l = [i for i in l if i != '']

    # question = input("Enter the question.")
    ps = PorterStemmer()
    ql = [ps.stem(i.lower()) for i in question.split() if len(i) > 3]

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

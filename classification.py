from math import sqrt, exp
from random import shuffle

import csv
with open('iris.data', 'r', newline=None) as source:
    lecteur = csv.reader(source)
    dataset = []
    for line in lecteur:
        for k in range(4):
            line[k] = float(line[k])
        dataset.append(line)

def dist(a, b):
    return sqrt( sum((a[i]-b[i])**2 for i in range(len(a))) )

def kppv(x, k):
    ldists = [dist(x, fleur[:4]) for fleur in dataset]
    bests = sorted(list(range(k)), key=lambda i : ldists[i])
    for i in range(k, len(ldists)):
        if ldists[i] < ldists[bests[-1]]:
            bests[-1] = i
            p = k - 1
            while p > 0 and ldists[bests[p]] < ldists[bests[p-1]]:
                bests[p], bests[p-1] = bests[p-1], bests[p]
    return bests

def prediction(ivoisins):
    choix = {}
    for i in ivoisins:
        typeFleur = dataset[i][4]
        effectif = choix.get(typeFleur, 0)
        choix[typeFleur] = effectif + 1
    return max(choix.keys(), key=lambda t : choix[t])

print( [dataset[i] for i in kppv([5,2.9,1.3], 3)])
print( prediction(kppv([5,2.9,1.3], 3)) )

#!/usr/bin/env python
# coding : utf-8


## Exercice 10


def rendu(somme: int, pieces: list) -> list:
    i = len(pieces) - 1
    rendre = []
    while somme > 0 and i > -1:
        piece = pieces[i]
        if piece <= somme:
            rendre.append(piece)
            somme -= piece
        else:
            i -= 1
    return rendre


print(rendu(493, [1, 2, 5, 10, 20, 50, 100, 200, 500]))


## Exercice 11


def sac_glouton(poidsMax: float, vps: list) -> list:
    vps.sort(key=lambda vp: vp[0] / vp[1], reverse=True)
    sac = []
    for (v, p) in vps:
        if p <= poidsMax:
            sac.append((v, p))
            poidsMax -= p
    return sac


print(sac_glouton(30, [(7, 13), (4, 12), (3, 8), (3, 10)]))


## Exercice 12
import matplotlib.pyplot as plt


def angleDirect(A: tuple, B: tuple, C: tuple, D: tuple) -> bool:
    xA, yA = A
    xB, yB = B
    xC, yC = C
    xD, yD = D

    det = (xB - xA) * (yD - yC) - (yB - yA) * (xD - xC)
    return det > 0


def enveloppeConvexe(points: list) -> list:
    premierPoint = min(points)
    enveloppe = [premierPoint]
    dernierPoint = premierPoint
    fini = False
    while not fini:
        pointMin = points[0]
        for point in points[1:]:
            if point != dernierPoint and angleDirect(
                dernierPoint, point, dernierPoint, pointMin
            ):
                pointMin = point
        dernierPoint = pointMin
        enveloppe.append(pointMin)
        if pointMin == premierPoint:
            fini = True
    return enveloppe


import random

# points = [(random.random()*400, random.random()*400) for _ in range(50)]

# env = enveloppeConvexe(points)

# plt.close('all')
# plt.figure("Une enveloppe convexe")
# plt.plot([p[0] for p in points], [p[1] for p in points], '*')
# plt.plot([p[0] for p in env], [p[1] for p in env], '-')
# plt.show()


## Exercice 13

def hanoi(n, debut, inter, fin):
    if n == 0: return
    hanoi(n-1, debut, fin ,inter)
    print(f'{debut} ---> {fin}')
    hanoi(n-1, inter, debut, fin)

hanoi(4,'A','B','C')

## Exercice 14

operations = [
    ("+", lambda x, y: x + y),
    ("-", lambda x, y: x - y),
    ("*", lambda x, y: x * y),
    ("/", lambda x, y: x // y),
]


def leCompte(cible, nombres):
    nombres.sort(reverse=True)
    if len(nombres) < 2:
        return
    for i in range(len(nombres)):
        for j in range(len(nombres)):
            if i == j:
                continue

            a, b = nombres[i], nombres[j]
            for (nom, op) in operations:
                resultat = op(a, b)
                if nom == "/" and resultat * b != a:
                    continue

                if resultat == cible:
                    return [f"{a} {nom} {b} = {resultat}"]
                elif resultat != 0:
                    nouvNombres = nombres.copy()
                    del nouvNombres[max(i, j)]
                    del nouvNombres[min(i, j)]
                    nouvNombres.append(resultat)
                    suite_ops = leCompte(cible, nouvNombres)
                    if suite_ops != None:
                        return [f"{a} {nom} {b} = {resultat}"] + suite_ops


cible = random.randint(1, 999)
nombres = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100], k=6)
print(
    "cible =",
    cible,
    "; nombres fournis :",
    nombres,
    "\nSolution :",
    leCompte(cible, nombres),
)


## Exercice 15


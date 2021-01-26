#!/usr/bin/env python
# coding : utf-8

class Pile:
    def __init__(self):
        self.stack = []
    
    def est_vide(self):
        return len(self.stack) == 0

    def sommet(self):
        return self.stack[-1]
    
    def empile(self, x):
        self.stack.append(x)
    
    def depile(self):
        return self.stack.pop()

def tri_par_pile(xs):
    pile = Pile()
    triée = []
    i = 0
    while i < len(xs):
        if pile.est_vide() or xs[i] < pile.sommet():
            pile.empile(xs[i])
            i += 1
        else:
            triée.append(pile.depile())
    while not pile.est_vide():
        triée.append(pile.depile())
    return triée

def est_trié(xs):
    for i in range(len(xs)-1):
        if xs[i] > xs[i+1]:
            return False
    return True

# for L in [ [5,4,1,3,2], [3,4,1,2], [4,3,1,2,6,5], [4,5,3,7,2,1,6], [5,4,3,7,2,1,6] ]:
#     Ltrié = tri_par_pile(L)
#     if not est_trié(Ltrié):
#         print("Pas triée : " + str(L) + ", le résultat est : " + str(Ltrié))


def fusion(xs,ys):
    fusionné = []
    i, j = 0, 0
    while i < len(xs) and j < len(ys):
        if xs[i] <= ys[j]:
            fusionné.append(xs[i])
            i += 1
        else:
            fusionné.append(ys[j])
            j += 1
    if i < len(xs) :
        fusionné.extend(xs[i:])
    else:
        fusionné.extend(ys[j:])
    return fusionné

def tri_fusion(xs):
    taille = len(xs)
    if taille <= 1:
        return xs
    else:
        m = taille//2
        return fusion( tri_fusion(xs[:m]), tri_fusion(xs[m:]))

for L in [ [5,4,1,3,2], [3,4,1,2], [4,3,1,2,6,5], [4,5,3,7,2,1,6], [5,4,3,7,2,1,6] ]:
    Ltrié = tri_fusion(L)
    if not est_trié(Ltrié):
        print("Pas triée : " + str(L) + ", le résultat est : " + str(Ltrié))
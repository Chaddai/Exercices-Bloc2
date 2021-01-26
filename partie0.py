#!/usr/bin/env python
# coding : utf-8
import time

## Exercice 1

def factiteratif(n):
    p=1
    for i in range(2,n+1):
        p *= i
    return p

def factrecursif(n):
    if n==0:
        return 1
    else :
        return factrecursif(n-1)*n

def timeit(f, args, rep=1):
    start = time.time()
    for k in range(rep):
        f(*args)
    end = time.time()
    return end - start

print("500! par Itération :", timeit(factiteratif, [500], 1000))
print("500! par Récursion :", timeit(factrecursif, [500], 1000))

def fibiter(n):
    p0 = 1
    p1 = 1
    for i in range(2,n+1):
        p0, p1 = p1, p0+p1
    return p1

def fibrecur(n):
    if n==0 or n==1:
        return 1
    else:
        return fibrecur(n-1) + fibrecur(n-2)

print("fib(20) par Itération :", timeit(fibiter, [20], 100))
print("fib(20) par Récursion :", timeit(fibrecur, [20], 100))


## Exercice 2

def binomiter(n,p):
    b = 1
    for k in range(p):
        b *= (n-k)/(k+1)
    return round(b)

def binomial(n,p):
    if n>p and p>0:
        return binomial(n-1,p-1) + binomial(n-1,p)
    elif n==p or p==0:
        return 1
    else:
        return 0

print("binom(20, 5) :", binomial(20, 5), binomiter(20, 5))
print("binom(20, 5) par Itération :", timeit(binomiter, [20, 5], 100))
print("binom(20, 5) par Récursion :", timeit(binomial, [20, 5], 100))

def syriter(x, n):
    for k in range(n-1):
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x+1
    return x

def syrecur(x, n):
    if n <= 1:
        return x
    elif x % 2 == 0:
        return syrecur(x//2, n-1)
    else:
        return syrecur(3*x+1, n-1)

print("syr(500, 800) :", syrecur(500, 800), syriter(500, 800))
print("syr(500, 800) par Itération :", timeit(syriter, [500, 800], 1000))
print("syr(500, 800) par Récursion :", timeit(syrecur, [500, 800], 1000))


## Exercice 3

def minMax(xs):
    """Calcule le minimum et le maximum d'un tableau de valeur xs (non-vide !)"""
    min, max = xs[0], xs[0]
    for x in xs[1:]:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min,max

# ...


## Exercice 4

def binodyna(n,p):
    pascal = [[1]*(k+1) for k in range(n+1)]
    for k in range(2,n+1):
        for i in range(max(1,p - (n-k)),min(k,p+1)):
            pascal[k][i] = pascal[k-1][i-1] + pascal[k-1][i]
    return pascal[n][p]

print("binom(20, 5) :", binomial(20, 5), binodyna(20, 5))
print("binom(20, 5) par Dynamique :", timeit(binodyna, [20, 5], 100))
print("binom(20, 5) par Récursion :", timeit(binomial, [20, 5], 100))


# Exercice 6 
# O(log n) : recherche dichotomique dans un tableau trié
# O(n) : recherche linéaire dans un tableau OU renversement d'un tableau OU reconnaissance d'un palindrome, etc
# O(n log n) : tri fusion
# O(n^2) : élimination des doublons naïve OU tri par insertion/sélection/à bulles
# O(n^3) : multiplication naïve de matrice d'ordre n
# O(2^n) : recherche exhaustive dans une formule logique, backpack packing, les problèmes NP-complets

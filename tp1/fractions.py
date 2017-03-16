#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP1 Exercice 1
# Romain Gille E3FI
# Sujet :
#----------
#   1- Créer une classe Fraction
#   2- Implémenter l'algorithme d'euclide pour trouver le PGDC (plus grand
#       diviseur commun)
#
#   Voir https://deptinfo-ensip.univ-poitiers.fr/FILES/PDF/python1a.pdf
#
#   Implémenter ensuite ce PGDC de façon récursive.
#
#   3- dans la classe fraction, implémenter les operations
#
#       addition
#       soustraction
#       multiplication
#       division
#
#   La fraction obtenue à la fin doit être réduite, exemple
#
#
#   5/4 + 3/2 = 5/4 + 6/4 = 11/4
#   3/8 * 2/1 = 6/8 = 3/4
#----------


class Fraction:

    def __init__(self, n, d):
       self.n = n
       self.d = d


    def pgcd(self):
        newSelf = Fraction(abs(self.n), abs(self.d))

        if newSelf.n < 1 or newSelf.d < 1:
            return 1

        while newSelf.n != newSelf.d :
            if newSelf.n > newSelf.d :
                newSelf.n = newSelf.n - newSelf.d
            else :
                newSelf.d = newSelf.d - newSelf.n

        return newSelf.n


    def pgcdr(self, n, d):
        newSelf = Fraction(abs(n), abs(d))

        if newSelf.n < 1 or newSelf.d < 1:
            return 1

        if newSelf.n == newSelf.d:
            return newSelf.n

        elif newSelf.n > newSelf.d:
            return newSelf.pgcdr(newSelf.n - newSelf.d, newSelf.d)
        else:
            return newSelf.pgcdr(newSelf.n, newSelf.d - newSelf.n)


    def reduce(self):
        pgcd = self.pgcd()

        if pgcd != 0:
            return Fraction(self.n / pgcd, self.d / pgcd)
        else:
            return self


    def __add__(self, other):
        if type(other) is not Fraction:
            fraction = Fraction(other, 1)
        else:
            fraction = other

        if self.d != fraction.d:
            newSelf     = Fraction(self.n * fraction.d, self.d * fraction.d)
            newFraction = Fraction(fraction.n * self.d,fraction.d * self.d)

        return Fraction(newSelf.n + newFraction.n, newSelf.d).reduce()


    def __sub__(self, other):
        if type(other) is not Fraction:
            fraction = Fraction(other, 1)
        else:
            fraction = other

        if self.d != fraction.d:
            newSelf     = Fraction(self.n * fraction.d, self.d * fraction.d)
            newFraction = Fraction(fraction.n * self.d,fraction.d * self.d)

        return Fraction(newSelf.n - newFraction.n, newSelf.d).reduce()


    def __mul__(self, other):
        if type(other) is not Fraction:
            fraction = Fraction(other, 1)
        else:
            fraction = other

        newSelf     = Fraction(self.n, self.d)
        newFraction = Fraction(fraction.n, fraction.d)

        result      = Fraction(0, 0)
        result.n    = newSelf.n * newFraction.n
        result.d    = newSelf.d * newFraction.d

        return result.reduce()


    def __truediv__(self, other):
        if type(other) is not Fraction:
            fraction = Fraction(other, 1)
        else:
            fraction = other

        newSelf     = Fraction(self.n, self.d)
        newFraction = Fraction(fraction.n, fraction.d)

        result      = Fraction(0, 0)
        result.n    = newSelf.n / newFraction.n
        result.d    = newSelf.d / newFraction.d

        return result.reduce()

    def display(self):
        print(self.n, '/', self.d)

def main():
    f1 = Fraction(3, 5)
    f2 = Fraction(9, 2)
    print("Fraction 1 : ")
    f1.display()
    print("Fraction 2 : ")
    f2.display()
    print("Addition de ces deux fractions : ")
    f3 = f1 + f2
    f3.display()
    print("Soustraction du résultat à la première fraction : ")
    f4 = f3 - f1
    f4.display()
    print("Multiplication de ce dernier résultat à la deuxième fraction : ")
    f5 = f4 * f2
    f5.display()
    print("Division de ce résultat à la première fonction : ")
    f6 = f5 / f1
    f6.display()

if __name__ == "__main__":
    main()

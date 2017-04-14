#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP1 Exercice 1
# Romain Gille E3FI
# Sujet :
# ----------
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
# ----------

from __future__ import division


class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def pgcd(self):
        new_self = Fraction(abs(self.n), abs(self.d))

        if new_self.n < 1 or new_self.d < 1:
            return 1

        while new_self.n != new_self.d:
            if new_self.n > new_self.d:
                new_self.n = new_self.n - new_self.d
            else:
                new_self.d = new_self.d - new_self.n

        return new_self.n

    @staticmethod
    def pgcdr(n, d):
        new_self = Fraction(abs(n), abs(d))

        if new_self.n < 1 or new_self.d < 1:
            return 1

        if new_self.n == new_self.d:
            return new_self.n

        elif new_self.n > new_self.d:
            return new_self.pgcdr(new_self.n - new_self.d, new_self.d)
        else:
            return new_self.pgcdr(new_self.n, new_self.d - new_self.n)

    def reduce(self):
        pgcd = self.pgcd()

        if pgcd != 0:
            return Fraction(self.n / pgcd, self.d / pgcd)
        else:
            return self

    def __add__(self, other):
        new_self = Fraction(self.n, self.d)
        new_self.n = self.n * other.d + other.n * self.d
        new_self.d = self.d * other.d
        return new_self.reduce()

    def __sub__(self, other):
        new_self = Fraction(self.n, self.d)
        new_self.n = self.n * other.d - other.n * self.d
        new_self.d = self.d * other.d
        return new_self.reduce()

    def __mul__(self, other):
        new_self = Fraction(self.n, self.d)
        new_self.n = self.n * other.n
        new_self.d = self.d * other.d
        return new_self.reduce()

    def __truediv__(self, other):
        inverse = Fraction(other.d, other.n)
        new_self = Fraction(inverse.n * self.n, inverse.d * self.d)
        return new_self.reduce()

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

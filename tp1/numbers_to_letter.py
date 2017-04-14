#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP1 Exercice 2
# Romain Gille E3FI
# Sujet :
#   Un Australien à écrit chaque nombre de 1 à 1 000 000 en toutes lettres,
#   pas en chiffres sur sa machine à écrire. Cela lui a prit 16 années.
#   A vous de réitérer cet exploit et afficher le resultat à votre écran en
#   moins de temps que ce monsieur et en FRANCAIS.


def number_to_letters(size):
    result = ""
    size = str(size)

    for i in range(0, len(size)):
        number = size[i]

        k = ""
        if 2 == (len(size) - i) % 3:
            if number == '1':
                k = "dix"
            elif number == '2':
                k = "vingt"
            elif number == '3':
                k = "trente"
            elif number == '4':
                k = "quarante"
            elif number == '5':
                k = "cinquante"
            elif number == '6':
                k = "soixante"
            elif number == '7':
                k = "soixante dix"
            elif number == '8':
                k = "quatre vingt"
            elif number == '9':
                k = "quatre vingt  dix"
        elif 1 == (len(size) - i) % 3 or 0 == (len(size) - i) % 3:
            if number == '1':
                k = "un"
            elif number == '2':
                k = "deux"
            elif number == '3':
                k = "trois"
            elif number == '4':
                k = "quatre"
            elif number == '5':
                k = "cinq"
            elif number == '6':
                k = "six"
            elif number == '7':
                k = "sept"
            elif number == '8':
                k = "huit"
            elif number == '9':
                k = "neuf"

        if 0 == (len(size) - i) % 3:
            k += " cent"
        elif 0 == (len(size) - i) % 4 and (len(size) - i) < 7:
            k += " mille"
        elif 0 == (len(size) - i) % 7:
            k += " millions"

        result += k + " "

        result = result.replace("dix un", "onze")
        result = result.replace("dix deux", "douze")
        result = result.replace("dix trois", "treize")
        result = result.replace("dix quatre", "quatorze")
        result = result.replace("dix cinq", "quinze")
        result = result.replace("dix six", "seize")
        result = result.replace("soixante dix un", "soixante et onze")
        result = result.replace("soixante dix deux", "soixante douze")
        result = result.replace("soixante dix trois", "soixante treize")
        result = result.replace("soixante dix quatre", "soixante quatorze")
        result = result.replace("soixante dix cinq", "soixante quinze")
        result = result.replace("soixante dix six", "soixante seize")
        result = result.replace("quatre vingt dix un", "quatre vingt onze")
        result = result.replace("quatre vingt dix deux", "quatre vingt douze")
        result = result.replace("quatre vingt dix trois", "quatre vingt treize")
        result = result.replace("quatre vingt dix quatre", "quatre vingt quatorze")
        result = result.replace("quatre vingt dix cinq", "quatre vingt quinze")
        result = result.replace("quatre vingt dix six", "quatre vingt seize")
        result = result.replace("un cent", "cent")
        result = result.replace("un mille", "mille")

    return result


def main():
    for i in range(1, 1000000):
        print(number_to_letters(i))


if __name__ == "__main__":
    main()

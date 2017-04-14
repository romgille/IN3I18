#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP2 Exercice 1
# Romain Gille E3FI
# Sujet :
#   a - Ouvrir le fichier "mbox_short.txt" reçu par mail et transmis à
#       "e3fi@esiee.fr" et afficher le nombre de caractères présents dans le
#       fichier.
#   b - Nettoyez un peu le fichier en retirant les ponctuations (, ; / - _)
#       ainsi que les lettres seules (grâce aux expressions régulières).
#   c - Comptez le nombre d'occurence des différents mots du fichier nettoyé et
#       ne retournez que les 10 mots les plus présents.
#   d - Enregistrer la liste des mails contenus dans "mbox_short.txt"
#       (récupérés grâce aux expressions régulières) et les écrire dans un
#       fichier "contactstp2.csv" qu'il vous faut créer et dans lequel doivent
#       figurer (une seule fois) tous les mails (séparés pardes ";")
#   e - Effectuer le même traitement appliqué au fichier "mbox.txt" et comparez
#       le temps de traitement de chaque fichier.

import re
from time import time


def write_addresses_to_file(contacts, file):
    f = open(file, 'w')
    for address in contacts:
        f.write(address)
        f.write(';')
    f.close()
    return 0


def find_email_address(file):
    email = re.compile('([\w.]+@[\w.]+)')
    email_match = email.findall(file)
    contact = []
    for address in email_match:
        contact.append(re.sub('<|>', '', address))
    return contact


def suppress_double_element_in_list(input):
    new_list = list(set(input))
    return new_list


def store_words(file):
    dic = {}
    for word in file.split():
        if word. isdigit():
            continue
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


def show_most_used_words(dic):
    sorted_list = sorted([(value, key) for (key, value) in dic.items()])
    most_used_words = []
    for i in range(1, 10):
        most_used_words.append(sorted_list[-i][1])
    return most_used_words


def replace_punctuation(file):
    punctuation = re.compile('([,;/-_+!#$%^&*()|<>:])|( \w )')
    new_file = punctuation.sub(' ', file)
    return new_file


def count_char(file):
    count = 0
    for line in file:
        for _ in line:
            count += 1
    return count


def read_file(file):
    return file.read()


def open_file_for_reading(file_path):
    f = open(file_path, 'r')
    return f


def main():
    start_time_short = time()
    f = open_file_for_reading('./mbox_short.txt')
    file = read_file(f)
    contacts = suppress_double_element_in_list(find_email_address(file))
    write_addresses_to_file(contacts, 'contactstp2_short.csv')
    end_time_short = time()
    elapsed_time_short = end_time_short - start_time_short
    print("mbox short")
    print(elapsed_time_short)

    start_time_short = time()
    f = open_file_for_reading('./mbox.txt')
    file = read_file(f)
    contacts = suppress_double_element_in_list(find_email_address(file))
    write_addresses_to_file(contacts, 'contactstp2.csv')
    end_time_short = time()
    elapsed_time_short = end_time_short - start_time_short
    print("mbox")
    print(elapsed_time_short)


if __name__ == '__main__':
    main()

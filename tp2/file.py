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


import sys
import re
from time import time

def writeAddressesToFile(contacts, file):
    f = open(file, 'w')
    for address in contacts:
        f.write(address)
        f.write(';')
    f.close()
    return 0

def findEmailAddress(file):
    email = re.compile('([\w\.]+@[\w\.]+)')
    emailMatch = email.findall(file)
    contact = []
    for address in emailMatch:
        contact.append(re.sub('<|>', '', address))
    return contact

def suppressDoubleElementInList(input):
    newList = list(set(input))
    return newList

def storeWords(file):
    dic = {}
    for word in file.split():
        if(word.isdigit()):
            continue
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def showMostUsedWords(dic):
    sorted_list = sorted([(value,key) for (key,value) in dic.items()])
    mostUsedWords = []
    for i in range(1, 10):
        mostUsedWords.append(sorted_list[-i][1])
    return mostUsedWords

def replacePunctuation(file):
    punctuation = re.compile('(,|;|\/|-|_|\+|,|!|#|\$|%|\^|&|\*|\(|\)|\||<|>|:)|( \w ){1}')
    newFile = punctuation.sub(' ', file)
    return newFile

def countChar(file):
    count = 0
    for line in file:
        for char in line:
            count += 1
    return count

def readFile(file):
    return file.read()

def openFileForReading(filePath):
    f = open(filePath, 'r')
    return f

def main():
    start_time_short = time()
    f = openFileForReading('./mbox_short.txt')
    file = readFile(f)
    count = countChar(file)
    fileWithoutPunct = replacePunctuation(file)
    fileCountChar = countChar(fileWithoutPunct)
    dic = storeWords(fileWithoutPunct)
    mostUsedWords = showMostUsedWords(dic)
    contacts = suppressDoubleElementInList(findEmailAddress(file))
    writeAddressesToFile(contacts, 'contactstp2_short.csv')
    end_time_short = time()
    elapsed_time_short = end_time_short - start_time_short
    print(elapsed_time_short)

    start_time_short = time()
    f = openFileForReading('./mbox.txt')
    file = readFile(f)
    count = countChar(file)
    fileWithoutPunct = replacePunctuation(file)
    fileCountChar = countChar(fileWithoutPunct)
    dic = storeWords(fileWithoutPunct)
    mostUsedWords = showMostUsedWords(dic)
    contacts = suppressDoubleElementInList(findEmailAddress(file))
    writeAddressesToFile(contacts, 'contactstp2.csv')
    end_time_short = time()
    elapsed_time_short = end_time_short - start_time_short
    print(elapsed_time_short)

if __name__ == '__main__':
    main()

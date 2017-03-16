#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP2 Exercice 2
# Romain Gille E3FI
# Sujet :
#   a - Proposer une classe de liste doublement chaînée : deque
#   b - mettre en oeuvre les méthodes suivantes
#
#       push_first() : insertion au début
#       pop_first() : retrait au début
#       push_last() : insertion à la fin
#       pop_last() : retrait à la fin
#
#   c - Utiliser la deque pour détecter si une chaine de caractère est un
#       palindrome. Exemple
#
#       esoperesteicietserepose
#       ici
#       non
#       oui
#       amanaplanacanalpanama
#       ressasser
#
#       Fournissez le code pour mettre les lettres de la chaine de caractère
#       dans la liste doublement chaînée.
#
#   d - prétraiter la chaine pour enlever les espaces et tout réduire en
#       minuscule, puis tester si la chaine est un palindrome.
#
#       Esope reste ici et ce repose
#       A man a plan a canal Panama
#
#   e - De plus enlever accents et ponctuation
#       (virgules, points, exclamation, etc) et tester sur le texte suivant :
#       http://norvig.com/pal21txt.html

import re

class doublyLinkedNode:
    def __init__(self, prev, next, data):
        self.prev = prev
        self.next = next
        self.data = data

class doublyLinkedList:
    def __init__(self, firstNode, lastNode):
        self.firstNode = firstNode
        self.lastNode = lastNode

    def push_first(self, data):
        if self.firstNode != None:
            newNode = doublyLinkedNode(None, self.firstNode, data)
            self.firstNode.prev = newNode
            self.firstNode = newNode
        else:
            newNode = doublyLinkedNode(None, None, data)
            self.firstNode = newNode
            self.lastNode = newNode

    def pop_first(self):
        if self.firstNode != None:
            self.firstNode = self.firstNode.next

    def push_last(self, data):
        if self.lastNode != None:
            newNode = doublyLinkedNode(self.lastNode, None, data)
            self.lastNode.next = newNode
            self.lastNode = newNode
        else:
            newNode = doublyLinkedNode(None, None, data)
            self.lastNode = newNode
            self.firstNode = newNode

    def pop_first(self):
        if self.lastNode != None:
            self.lastNode = self.lastNode.prev

def isPalindrome(string):
    if not string.isalpha():
        string = re.sub('(?:\W)', '', string)

    if not string.islower():
        string = string.lower()

    dLL = doublyLinkedList(None, None)
    for i in string:
        dLL.push_last(i)

    node1 = dLL.firstNode
    node2 = dLL.lastNode

    while node1.data == node2.data:
        if node1 == node2:
            return 'C\'est un palindrome \n'
        else:
            node1 = node1.next
            node2 = node2.prev
    return 'Ce n\'est pas un palindrome \n'



def main():
    strings = [
        'Esope reste ici et se repose', 'A man a plan a canal Panama',
        'http://norvig.com/pal21txt.html'
    ]

    for string in strings:
        print(string)
        print(isPalindrome(string))

if __name__ == '__main__':
    main()

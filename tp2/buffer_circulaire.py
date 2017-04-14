#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP2 Exercice 3
# Romain Gille E3FI
# Sujet :
# Buffer circulaire
#
# http://fr.wikipedia.org/wiki/Buffer_circulaire
# http://en.wikipedia.org/wiki/Circular_buffer
#
# 1- Mettre en oeuvre le tableau circulaire vu en cours à l'aide d'un tableau
# =======================================================
#
# a - créez une classe CircBuf
# b- prévoyez les méthodes suivantes
#
#     push(): ajouter un élement au buffer
#     erase() : effacement complet
#
# 2- à la création de la classe, on demande à l'utilisateur une taille maximum.
# =========================================================
#
# - dans un premier temps si l'utilisateur tente d'insérer un élément de trop, on retourne une erreur - dans un
# second temps, prévoyez le redimensionnement du tableau circulaire. Quelle est la complexité de cette opération ?
# Quelle stratégie de redimensionnement proposez vous ? On peut par exemple ajouter une taille fixe au tableau
# circulaire, ou bien doubler la taille courante. Laquelle vous paraît préférable ?
#
#     - prévoyez les méthodes suivantes:
#
#     augment() : augmente la taille du buffer d'une constante, ou double la taille
#     shrink() : diminue la taille du buffer d'une constante, ou divise la taille par deux.
#
# 3- Utilisation
# =========
#
#     Prévoyez les cas d'erreur.
#     Donnez les tests de votre structure de données.


class Node:
    def __init__(self, value=None, previousNode=None, nextNode=None):
        self.previous = previousNode
        self.next = nextNode
        self.value = value
        if previousNode is not None:
            previousNode.next = self
        if nextNode is not None:
            nextNode.previous = self


class CircBuf:
    def __init__(self, size):
        self.size = size
        self.currentSize = 0
        node = Node()
        self.currentNode = node
        self.firstNode = node
        self.lastNode = node
        n = self.firstNode
        for i in range(size - 1):
            n = Node(previousNode=n)
        n.next = self.firstNode
        self.firstNode.previous = n

    def to_string(self):
        s = ""
        node = self.firstNode
        for i in range(self.size):
            s += str(i) + ": " + str(node.value) + "\n"
            node = node.next
        return s

    def push(self, value):
        if self.currentSize >= self.size:
            raise NameError('Out of bounds Exception')
        self.currentNode.value = value
        self.currentNode = self.currentNode.next
        self.currentSize += 1

    def pop(self):
        self.lastNode.value = None
        self.lastNode = self.lastNode.next
        self.currentSize -= 1

    def erase(self):
        for i in range(self.size):
            self.pop()
        self.currentSize = 0

    def augment(self, size):
        for i in range(size):
            Node(previousNode=self.currentNode, nextNode=self.currentNode.next)
        self.size += size

    def shrink(self, size):
        for i in range(size):
            if self.firstNode.value is not None:
                self.currentSize -= 1
            if self.currentNode == self.firstNode:
                self.currentNode = self.firstNode.next
            if self.lastNode == self.firstNode:
                self.lastNode = self.firstNode.next
            self.firstNode.next.previous = self.firstNode.previous
            self.firstNode.previous.next = self.firstNode.next
            self.firstNode = self.firstNode.next
        self.size -= size


buf = CircBuf(10)

for i in range(5):
    buf.push(i)
print (buf.to_string())

buf.shrink(6)
print (buf.to_string())
buf.push('a')
buf.push('b')
print (buf.to_string())
buf.pop()
print (buf.to_string())
buf.push('A')
buf.push('B')
buf.push('C')
print (buf.to_string())
buf.erase()
print (buf.to_string())
buf.push("Yeah")
print (buf.to_string())

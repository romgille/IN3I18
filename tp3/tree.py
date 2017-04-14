# coding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# TP3 Exercice 1
# Romain Gille E3FI
# Sujet :
# 1- Implantez une structure de tas, arbre binaire partiellement trié qu’il faut impérativement implémanter avec un
# tableau. faites une classe avec deux méthodes de base: downheap et upheap, et également le swap rapide entre deux
# éléments du tableau.
#
# https://fr.wikipedia.org/wiki/Tas_(informatique)
#
# Pour rajouter un élément dans le tas on ajoute à la fin du tableau et on fait upheap Pour enlever un élément on
# échange le dernier avec le premier, on sort le dernier (qui était le premier) et on fait downheap.
#
# ensuite il faut deux méthodes publiques:
#
#    insert() # insérer un élément dans le tas
#     delete() # sortir la racine du tas.
#
# ensuite avec ces deux opérations, implémentez le tri heapsort, qui est très simple: Etant donné un tableau
# d’éléments non triés, tout insérer dans le tas, puis tout enlever. Les  éléments apparaissent triés.
#
# Voir http://en.wikipedia.org/wiki/Binary_heap
#
# 2- Impémlentez l'algorithme bubble sort. Comparer heapsort et bubble sort pour des tableaux de taille croissante
# entre 10 et 10^5 éléments. Faire un plot log-log comparant les deux méthodes.
#
# === Exercice 5 ===
#
# 1- terminer heapsort sur un tableau, sans utiliser de stockage supplémentaire(cf rechercher in-place heapsort).
# C’est assez simple, il faut séparer le tableau initial en deux parties: la partie utilisé par le tas et par le
# reste du tableau, aussi bien au moment de la création du tas que de sa destruction. Quand on construit le tas on
# lit le tableau de longueur n+1, de gauche à droite. A l’indice i on construit le tas dans la partie de 0 à i-1,
# avec le reste du tableau entre i et n. Pour la deuxième phase, celle de tri, dans l’algorithme du tas on échange la
#  racine (le plus grand élément) avec la fin du tas, puis on réduit le tas et on fait les permutations pour
# continuer à garantir la condition de tas. Cette façon de faire place naturellement l’élément le plus grand du tas à
#  l’endroit du tableau qu’il faut pour qu’il soit trié (a la fin pour le plus grand element, puis juste avant pour
# le 2e plus grand, etc).
#
# C’est très important quand on utilise beaucoup de mémoire. C’est très joli à faire, les deux parties du tri (mise
# dans le tas et extraction) sont assez élégantes.
#
# Une autre façon de faire encore plus efficace consiste à prendre les valeurs initiales, non-triées du tableau et
# faire uniquement les permutations nécessaires pour que la condition de tas soit respectée, en place,
# dans le tableau. Il suffit de le faire des feuilles vers la racine et c’est très rapide.  Ensuite on extrait les
# valeurs du tas comme précédemment.
#
# Comparez le temps de calcul des différentes versions de heapsort.
#
# 2- En utilisant la classe deque codée au TP précédent. Impémentez les algos de mergesort et de tri par fusion
#
# http://en.wikipedia.org/wiki/Merge_sort (Il y a de nombreux exemples d’implementation dans cette page, mais le cas
# de la liste est celui de l’animation, qu’ils appellent top-down par liste)
#
# http://fr.wikipedia.org/wiki/Tri_fusion
#
# Comparez les temps d'exécution pour une liste donnée des différents algorithmes de tri d'une liste.

from time import time


class Node:
    def __init__(self, value, previousNode=None, nextNode=None):
        self.previous = previousNode
        self.next = nextNode
        self.value = value
        if previousNode is not None:
            previousNode.next = self
        if nextNode is not None:
            nextNode.previous = self


class Deque:
    @staticmethod
    def from_string(string):
        deque = Deque()
        string = string.strip().lower()

        for c in string:
            deque.push_last(c)
        deque.pop_first()

        return deque

    def __init__(self, value=None):
        node = Node(value)
        self.currentNode = node
        self.firstNode = node
        self.lastNode = node
        self.count = 1

    def to_string(self):
        s = ""
        node = self.firstNode
        while node is not None:
            s += node.value
            node = node.next
        return s

    def push_first(self, value):
        self.firstNode = Node(value, nextNode=self.firstNode)
        self.count += 1

    def pop_first(self):
        self.firstNode = self.firstNode.next
        self.firstNode.previous = None
        self.count -= 1

    def push_last(self, value):
        self.lastNode = Node(value, previousNode=self.lastNode)
        self.count += 1

    def pop_last(self):
        self.lastNode = self.lastNode.previous
        self.lastNode.next = None
        self.count -= 1

    def get(self, index):
        if index > self.count - 1:
            raise Exception('Out of bound exception')
        r = self.firstNode
        for i in range(index):
            r = r.next
        return r

    def to_array(self):
        array = []
        n = self.firstNode
        while n is not None:
            array.append(n.value)
            n = n.next
        return array


def bubblesort(vals):
    sortedArray = list(vals)
    for i in range(len(sortedArray) - 1, 0, -1):
        for j in range(i):
            if sortedArray[j] > sortedArray[j + 1]:
                sortedArray[j], sortedArray[j + 1] = sortedArray[j + 1], sortedArray[j]
    return sortedArray


def mergesort(vals):
    def merge(left, right):
        mergedArray = list()
        while len(left) != 0 and len(right) != 0:
            if left[0] <= right[0]:
                mergedArray.append(left[0])
                left.pop(0)
            else:
                mergedArray.append(right[0])
                right.pop(0)
        while len(left) != 0:
            mergedArray.append(left[0])
            left.pop(0)
        while len(right) != 0:
            mergedArray.append(right[0])
            right.pop(0)
        return mergedArray

    sortedArray = list(vals)
    if len(sortedArray) <= 1:
        return sortedArray

    left, right = list(), list()
    for i in range(len(sortedArray)):
        if i % 2 != 0:
            left.append(sortedArray[i])
        else:
            right.append(sortedArray[i])

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def main():
    d = Deque(1)
    d.push_last(8)
    d.push_last(4)
    d.push_first(19)

    print (d.to_array())
    start_time_bubble = time()
    bubble = bubblesort(d.to_array())
    stop_time_bubble = time()
    elapsed_time_bubble = stop_time_bubble - start_time_bubble
    print("bubble")
    print(bubble)
    print(elapsed_time_bubble)
    start_time_merge = time()
    merge = mergesort(d.to_array())
    stop_time_merge = time()
    elapsed_time_merge = stop_time_merge - start_time_merge
    print("merge")
    print(merge)
    print(elapsed_time_merge)

if __name__ == '__main__':
    main()



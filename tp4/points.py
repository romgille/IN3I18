import math
from random import randint
from time import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + " ; y: " + str(self.y)

    def __repr__(self):
        return '( ' + self.__str__() + ' )'

    def same_as(self, other):
        return self.x == other.x and self.y == other.y


def print_list(l):
    for i in range(len(l)):
        print (l[i])


def dist(p1, p2):
    return math.sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))


def find_closest(points):
    if len(points) < 2:
        raise Exception('can\'t find other point')

    p1, p2 = points[0], points[1]
    smallestdist = dist(points[0], points[1])

    for i in points:
        for j in points:
            if i.same_as(j):
                continue
            d = dist(i, j)
            if d < smallestdist:
                smallestdist = d
                p1 = i
                p2 = j
    return p1, p2


def find_closest_better(points, max_x, max_y):
    lists = list()

    lists.append(list())
    lists.append(list())
    lists.append(list())
    lists.append(list())
    for p in points:
        if p.x < max_x / 2 and p.y < max_y / 2:
            lists[0].append(p)
        elif p.x < max_x / 2 and p.y >= max_y / 2:
            lists[1].append(p)
        elif p.x >= max_x / 2 and p.y < max_y / 2:
            lists[2].append(p)
        else:
            lists[3].append(p)

    lists.append(list())
    lists.append(list())
    lists.append(list())
    lists.append(list())
    for p in points:
        if max_x / 4 < p.x < (max_x - max_x / 4) and p.y < max_y / 2:
            lists[4].append(p)
        elif max_x / 4 < p.x < (max_x - max_x / 4) and p.y >= max_y / 2:
            lists[5].append(p)
        elif p.x < max_x / 2 and max_y / 4 < p.y < (max_y - max_y / 4):
            lists[6].append(p)
        elif p.x > max_x / 2 and max_y / 4 < p.y < (max_y - max_y / 4):
            lists[7].append(p)

    lists.append(list())
    for p in points:
        if max_x / 4 < p.x < (max_x - max_x / 4) and max_y / 4 < p.y < (max_y - max_y / 4):
            lists[8].append(p)

    mins = list()
    for l in lists:
        if len(l) > 1:
            p1, p2 = find_closest(l)
            mins.append(p1)
            mins.append(p2)

    return find_closest(mins)


def main():
    points = list()
    max_x = 100
    max_y = 100

    for i in range(1000):
        points.append(Point(randint(0, max_x), randint(0, max_y)))

    start_time_normal = time()
    normal = find_closest(points)
    stop_time_normal = time()
    elapsed_time_normal = stop_time_normal - start_time_normal
    print("normal")
    print(normal)
    print(elapsed_time_normal)

    start_time_better = time()
    better = find_closest_better(points, max_x, max_y)
    stop_time_better = time()
    elapsed_time_better = stop_time_better - start_time_better
    print("better")
    print(better)
    print(elapsed_time_better)

if __name__ == '__main__':
    main()

from random import randint
from time import time


class Fifo:
    def __init__(self, value=None):
        self.value = value
        self.values = list()

    def __str__(self):
        s = "stack size: " + str(len(self.values)) + "\n"
        for i in range(len(self.values)):
            s += str(self.values[i]) + " "
        return s

    def pop(self):
        self.values.pop(0)

    def push(self, value):
        self.values.append(value)


def insertsort(vals):
    sortedArray = list(vals)
    for i in range(0, len(sortedArray)):
        j = i
        while j > 0 and sortedArray[j - 1] > sortedArray[j]:
            sortedArray[j], sortedArray[j - 1] = sortedArray[j - 1], sortedArray[j]
            j -= 1
    return sortedArray


def bucketsort(vals):
    nbBuckets = 25
    buckets = list()
    for i in range(nbBuckets):
        buckets.append(list())
        buckets[i] = list()
    for i in range(len(vals)):
        buckets[int(vals[i] / nbBuckets)].append(vals[i])
    for i in range(nbBuckets):
        buckets[i] = insertsort(buckets[i])
    sortedArray = list()
    for i in range(nbBuckets):
        for j in range(len(buckets[i])):
            sortedArray.append(buckets[i][j])
    return sortedArray


def main():
    stack = Fifo()
    for i in range(randint(10, 100)):
        stack.push(randint(0, 100))

    print (stack)
    start_time_insert = time()
    insert = insertsort(stack.values)
    stop_time_insert = time()
    elapsed_time_insert = stop_time_insert - start_time_insert
    print("insert")
    print(insert)
    print(elapsed_time_insert)

    start_time_bucket = time()
    bucket = bucketsort(stack.values)
    stop_time_bucket = time()
    elapsed_time_bucket = stop_time_bucket - start_time_bucket
    print("bucket")
    print(bucket)
    print(elapsed_time_bucket)


if __name__ == '__main__':
    main()

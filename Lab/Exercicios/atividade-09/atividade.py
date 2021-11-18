#Gere e ordene vetores de 10, 100, 1000, 10000, 1000000 elementos contando o tempo de execuçao e quantidade de comparaçoes realizadas utilizando o MergeSort.import time
import numpy as np
import sys


def mergeSort(aList):
    if len(aList) > 1:
        mid = len(aList)//2
        L = aList[:mid]
        R = aList[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                aList[k] = L[i]
                i += 1
            else:
                aList[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            aList[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            aList[k] = R[j]
            j += 1
            k += 1


def main():

    start = time.time()
    one = np.ndarray.tolist(np.random.randint(1000, size = 10))
    mergeSort(one, 0, len(one)-1)
    final = time.time()
    print("10 elementos:", final - start)

    start = time.time()
    two = np.ndarray.tolist(np.random.randint(1000, size = 100))
    mergeSort(two, 0, len(two)-1)
    final = time.time()
    print("100 elementos:", final - start)

    start = time.time()
    three = np.ndarray.tolist(np.random.randint(1000, size = 1000))
    mergeSort(three, 0, len(three)-1)
    final = time.time()
    print("1000 elementos:", final - start)

    start = time.time()
    four = np.ndarray.tolist(np.random.randint(1000, size = 10000))
    mergeSort(four, 0, len(four)-1)
    final = time.time()
    print("10000 elementos:", final - start)

    start = time.time()
    five = np.ndarray.tolist(np.random.randint(1000, size = 1000000))
    mergeSort(five, 0, len(five)-1)
    final = time.time()
    print("1000000 elementos:", final - start)

rec = sys.getrecursionlimit()
sys.setrecursionlimit(100000)
main()
sys.setrecursionlimit(rec)
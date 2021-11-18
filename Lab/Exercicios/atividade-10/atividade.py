# Gere e ordene vetores de 10, 100, 1000, 10000, 1000000 elementos contando o tempo de execuçao e quantidade de comparaçoes realizadas utilizando o QuickSort.
import time
import numpy as np
import sys



def partition(aList, low, high):
    i = (low-1)
    pivot = aList[high]
    for j in range(low, high):
        if aList[j] <= pivot:
            i = i+1
            aList[i], aList[j] = aList[j], aList[i]
    aList[i+1], aList[high] = aList[high], aList[i+1]
    return (i+1)
def quickSort(aList, low, high):
    if len(aList) == 1:
        return aList
    if low < high:
        pi = partition(aList, low, high)
        quickSort(aList, low, pi-1)
        quickSort(aList, pi+1, high)




def main():

    start = time.time()
    one = np.ndarray.tolist(np.random.randint(1000, size = 10))
    quickSort(one, 0, len(one)-1)
    final = time.time()
    print("10 elementos:", final - start)

    start = time.time()
    two = np.ndarray.tolist(np.random.randint(1000, size = 100))
    quickSort(two, 0, len(two)-1)
    final = time.time()
    print("100 elementos:", final - start)

    start = time.time()
    three = np.ndarray.tolist(np.random.randint(1000, size = 1000))
    quickSort(three, 0, len(three)-1)
    final = time.time()
    print("1000 elementos:", final - start)

    start = time.time()
    four = np.ndarray.tolist(np.random.randint(1000, size = 10000))
    quickSort(four, 0, len(four)-1)
    final = time.time()
    print("10000 elementos:", final - start)

    start = time.time()
    five = np.ndarray.tolist(np.random.randint(1000, size = 1000000))
    quickSort(five, 0, len(five)-1)
    final = time.time()
    print("1000000 elementos:", final - start)

rec = sys.getrecursionlimit()
sys.setrecursionlimit(100000)
main()
sys.setrecursionlimit(rec)
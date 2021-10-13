import numpy as np
import matplotlib.pyplot as plt
import time

def ex1():
    # 1) Na busca linear implementada em aula, o algoritmo tentava encontrar a primeira ocorrência do elemento procurado. Queremos agora encontrar a última ocorrência (caso exista) de um determinado elemento. Para isto, desenvolva a função:
    #       def linearSearchLast(L, e):
    # que devolva, caso exista, o último índice ocupado pelo elemento e na lista L. Caso o elemento não exista na lista, a função deverá retornar -1
    def linearSearchLast(L, e):
        find = False
        for i in range(len(L)):
            if L[i] == e: 
                find = True
                lastIndex = i
        if find: return lastIndex
        return -1
    lista = [1,2,3,4,4,6]
    ultimaOcorrencia = linearSearchLast(lista, 4)
    print(f"Última ocorrência: {ultimaOcorrencia}")
ex1()

def ex2():
    #2) 
    # Modifique o programa de busca sequencial para contar quantas comparações são feitas durante a busca. 
    # Teste a sua modificação e conte quantas operações são feitas para listas de tamanho 10, 50, 100, 500, 1000, 5000, 10000, 50000 e 100000.
    # Gere um gráfico tamanho da lista x número de comparações
    def linearSearch(aList, element):
        count = 0 
        for i in range(len(aList)):
            count += 1
            if aList[i] == element:
                return i, count
        return -1, count
    def generateLists():
        lists = []
        value = 10
        multiplier = 5
        for i in range(9):
            aList = np.arange(0, value)
            aList = np.ndarray.tolist(aList)
            value = value * multiplier
            multiplier = 2 if multiplier == 5 else 5
            lists.append(aList)
        return lists
    def getComparsions(lists):
        comparsions = []
        for list in lists: 
            result = linearSearch(list, 9999999999)
            comparsions.append(result[1])
        return comparsions
    def generateGraphic(x, y):
        plt.scatter(x,y)
        plt.plot(x,y)
        plt.show()
    lists = generateLists()
    comparsions = getComparsions(lists)
    generateGraphic(comparsions, [len(lista) for lista in lists])
    print(comparsions)
ex2()

def ex3():
    # 3) Estime o tempo médio para encontrar qualquer elemento em cada uma das listas do exercício anterior
    def linearSearch(aList, element):
        count = 0
        for i in range(len(aList)):
            count += 1
            if aList[i] == element:
                return i
        return -1
    def generateLists():
        lists = []
        value = 10
        multiplier = 5
        for i in range(9):
            aList = np.arange(0, value)
            aList = np.ndarray.tolist(aList)
            value = value * multiplier
            multiplier = 2 if multiplier == 5 else 5
            lists.append(aList)
        return lists
    def getComparsions(lists):
        start = time.time()
        for list in lists: 
            result = linearSearch(list, 9999999999)
            timeAfter = time.time() - start
            print(f"Tempo para a lista {len(list)}: {timeAfter}")
    getComparsions(generateLists())
ex3()

def ex4(): 
    # 4) Modifique o programa de busca binária iterativa para contar quantas comparações são feitas durante a busca. Teste a sua modificação e conte quantas operações são feitas para listas de tamanho 10, 50, 100, 500, 1000, 5000, 10000, 50000 e 100000. Gere um gráfico tamanho da lista x número de comparações. 
    def binarySearch(arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        comp = 0
        while low <= high:
            mid = (high + low) // 2
            comp += 1
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                comp += 1
                high = mid - 1
            else:
                return mid, comp
        return -1, comp
    def generateLists():
        lists = []
        value = 10
        multiplier = 5
        for i in range(9):
            aList = np.arange(0, value)
            aList = np.ndarray.tolist(aList)
            value = value * multiplier
            multiplier = 2 if multiplier == 5 else 5
            lists.append(aList)
        return lists
    def getComparsions(lists):
        comparsions = []
        for list in lists: 
            result = binarySearch(list, 9999999999)
            comparsions.append(result[1])
        return comparsions
    def generateGraphic(x, y):
        plt.scatter(x,y)
        plt.plot(x,y)
        plt.show()
    lists = generateLists()
    comparsions = getComparsions(lists)
    generateGraphic(comparsions, [len(lista) for lista in lists])
    print(comparsions)
ex4()

def ex5():
    # 3) Estime o tempo médio para encontrar qualquer elemento em cada uma das listas do exercício anterior
    def binarySearch(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid
                else:
                    return mid
            return -1
    def generateLists():
        lists = []
        value = 10
        multiplier = 5
        for i in range(9):
            aList = np.arange(0, value)
            aList = np.ndarray.tolist(aList)
            value = value * multiplier
            multiplier = 2 if multiplier == 5 else 5
            lists.append(aList)
        return lists
    def getComparsions(lists):
        start = time.time()
        for list in lists: 
            result = binarySearch(list, 9999999999)
            timeAfter = time.time() - start
            print(f"Tempo para a lista {len(list)}: {timeAfter}")
    getComparsions(generateLists())
ex3()
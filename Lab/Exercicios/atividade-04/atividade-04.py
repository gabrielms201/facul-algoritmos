import random
import time
import matplotlib.pyplot as plt
# > gere dados aleatórios (10, 100, 500, 1000, 5000, 10000) e salve-os em arquivos.
# > abra os arquivos, leia-os, carregue os valores em listas e ordene-as com os algoritmos bubble, insertion e selection.
# > realize a aferição temporal de cada ordenação.
# > plote os gráficos pertinentes para comparação dos tempos de execução.



class listMethods():
    def bubbleSort(aList):
        lastIndex = len(aList)-1
        for i in range(lastIndex, 0, -1):
            for j in range(lastIndex):
                if aList[j] > aList[j+1]:
                    aList[j], aList[j+1] = aList[j+1], aList[j]
        return aList
    def selectionSort(aList):
        for i in range(len(aList) - 1, 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if aList[j] > aList[maxIndex]:
                    maxIndex = j
            aList[i], aList[maxIndex] = aList[maxIndex], aList[i]
        return aList
    def insertionSort(aList):
        for i in range(1, len(aList)):
            j = i-1
            nextElement = aList[i]
            while (aList[j] > nextElement) and (j >= 0):
                aList[j+1] = aList[j]
                j-=1
                aList[j+1] = nextElement
        return aList
class listService():
    def generateFile(fileName):
        file = open(f"{fileName}.txt", "w+", encoding = "UTF-8")
        for i in range(10000):
            file.write(str(random.randint(0,10000)))
            file.write("\n")
        file.close()
    def generateList(fileName):
        file = open(f"{fileName}.txt", "r+", encoding = "UTF-8")
        aList = []
        for line in file:
            aList.append(int(line.rstrip()))
        file.close()
        return aList
def generateTime(shouldBubble = False, shouldSelect = False, shouldInsert = True):
    #listService.generateFile(""numbers"")
    lists = []
    for i in range(3):
        lists.append(listService.generateList("numbers"))
    times = []
    # Bubble Conditional
    if shouldBubble:
        tempoInicioBubble = time.time()
        bubble = listMethods.bubbleSort(lists[0])
        tempoBubble = time.time() - tempoInicioBubble
        times.append(tempoBubble)
    # Bubble 
    if shouldSelect:
        tempoInicioSelect = time.time()
        select = listMethods.selectionSort(lists[1])
        tempoSelect = time.time() - tempoInicioSelect
        times.append(tempoSelect)

    if shouldInsert:
        tempoInicioInsert = time.time()
        insert = listMethods.insertionSort(lists[2])
        tempoInsert = time.time() - tempoInicioInsert
        times.append(tempoInsert)
    
times = generateTime(True, True, True)



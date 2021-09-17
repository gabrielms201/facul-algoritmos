import random
import time
# > gere dados aleatórios (10, 100, 500, 1000, 5000, 10000) e salve-os em arquivos.
# > abra os arquivos, leia-os, carregue os valores em listas e ordene-as com os algoritmos bubble, insertion e selection.
# > realize a aferição temporal de cada ordenação.
# > plote os gráficos pertinentes para comparação dos tempos de execução.



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





def gerarLista():
    file = open("numbers.txt", "r")
    lista = []
    for linha in file:
        lista.append(int(linha.rstrip()))
    file.close()
    return lista
def a():
    tempoInicioBubble = time.time()
    bubble = bubbleSort(gerarLista())
    tempoBubble = time.time() - tempoInicioBubble
    print(tempoBubble)
def b():
    tempoInicioSelect = time.time()
    select = selectionSort(gerarLista())
    tempoSelect = time.time() - tempoInicioSelect
    print(tempoSelect)
def c():
    tempoInicioInsert = time.time()
    insert = insertionSort(gerarLista())
    tempoInsert = time.time() - tempoInicioInsert
    print(tempoInsert)
a()
b()
c()




        

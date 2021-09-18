import random
import time
import matplotlib.pyplot as plt
import numpy as np

# > gere dados aleatórios (10, 100, 500, 1000, 5000, 10000) e salve-os em arquivos.
# > abra os arquivos, leia-os, carregue os valores em listas e ordene-as com os algoritmos bubble, insertion e selection.
# > realize a aferição temporal de cada ordenação.
# > plote os gráficos pertinentes para comparação dos tempos de execução.


# > Lists:
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
    def generateFile(fileName, number = 10000):
        file = open(f"{fileName}.txt", "w+", encoding = "UTF-8")
        for i in range(number):
            file.write(str(random.randint(0,10000)))
            file.write("\n")
        file.close()
    def generateLists(fileName):
        lists = []
        for i in range(3):
            file = open(f"{fileName}.txt", "r+", encoding = "UTF-8")
            aList = []
            for line in file:
                aList.append(int(line.rstrip()))
            lists.append(aList)
            file.close()
        return lists
# > Time:
def generateTime(shouldBubble = True, shouldSelect = True, shouldInsert = True):
    lists = listService.generateLists("numbers")
    times = []
    # Bubble Conditional
    if shouldBubble:
        print("Ordenando por Bubble... Aguarde")
        start = time.time()
        listMethods.bubbleSort(lists[0])
        bubbleTime = time.time() - start
        times.append(bubbleTime)
    # Select Conditional
    if shouldSelect:
        print("Ordenando por Select... Aguarde")
        start = time.time()
        listMethods.selectionSort(lists[1])
        selectTime = time.time() - start
        times.append(selectTime)
    # Insert Conditional
    if shouldInsert:
        print("Ordenando por Insert... Aguarde")
        start = time.time()
        listMethods.insertionSort(lists[2])
        insertTime = time.time() - start
        times.append(insertTime)
    
    return times
# > Graphics:
def generateGraphic(times):
    # > Values
    sorts = ["BubbleSort", "SelectionSort", "InsertionSort"]
    x = np.arange(len(sorts))

    # > Graphic Plot
    plt.xticks(x, sorts)
    plt.bar(x, times, width=0.7, label="Tempo", color = "red")
    plt.ylabel("Tempo(s)")
    plt.xlabel("Algoritmo")
    plt.title("Métodos de Ordernar Lista")
    plt.legend()

    plt.show()

def main():
    generate = input("Deseja gerar o arquivo de texto? S/N ").upper()
    listService.generateFile(f"numbers") if generate == "S" else None
    times = generateTime(True, True, True)
    
    print(f"-> Bubble: {times[0]}")
    print(f"-> Selection: {times[1]}")
    print(f"-> Insertion: {times[2]}")
    
    generateGraphic(times)

main()

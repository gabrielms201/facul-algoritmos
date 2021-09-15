import random
import os

class Methods():
    def selectionSort(aList):
        for i in range(len(aList) -1 , 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if aList[j] > aList[maxIndex]: maxIndex = j
            aList[i], aList[maxIndex] = aList[maxIndex], aList[i]
        return aList
    
    def getAverage(aList, shouldSort = True):
        if shouldSort: Methods.selectionSort(aList)
        sum = 0
        listLen = len(aList)
        for element in aList: sum += element
        average = sum / listLen
        return average
    
    def getMedian(aList, shouldSort = True):
        if shouldSort: Methods.selectionSort(aList)
        listLen = len(aList)
        middleIndex = listLen // 2
        if listLen % 2 == 1: return aList[middleIndex]
        firstValue = aList[middleIndex] ; secondValue = aList[middleIndex - 1]
        median = (firstValue + secondValue) / 2
        return median

def firstExercise(fileDir):
    # Nho Lau está pesquisando seu rebanho para encontrar a vaca mais comum. Ele quer saber quanto leite esta vaca
    # 'mediana' dá: metade das vacas dá tanto ou mais que a mediana; metade dá tanto quanto ou menos.
    # Dado um número ímpar de vacas N (1 <= N <10.000) e sua produção de leite (1..1.000.000 em litros), encontre a
    # quantidade mediana de leite fornecida de modo que pelo menos metade das vacas dêem a mesma quantidade de
    # leite ou mais e em pelo menos metade dá o mesmo ou menos
    if not os.path.exists(fileDir): os.makedirs(fileDir)
    def setCows(outputName, count):
        filename = f"{fileDir}/{outputName}{count}.txt"
        file = open(filename, "w+", encoding = "UTF-8")
        for i in range(10000):
            endl = "\n"
            file.write(str (random.randint(1, 1000000)) + endl)
        file.close()
        return filename
    def fillCows(inputName):
        cows = []
        file = open(inputName, "r", encoding = "UTF-8")
        for line in file: cows.append(int(line.rstrip()))
        file.close()
        return cows
    for count in range(10):
        print("...")
        cowsFile = setCows("cows", count)
        cowsList = Methods.selectionSort(fillCows(cowsFile))
        median = Methods.getMedian(cowsList, False)
        print(f"Arquivo ({count}) >> Valor da mediana: {median}")
        print("...")
def secondExercise(fileDir):
    if not os.path.exists(fileDir): os.makedirs(fileDir)
def thirdExercise(fileDir):
    if not os.path.exists(fileDir): os.makedirs(fileDir)


def main(showFirst = True, showSecond = True, showThird = True):
    # 1-)
    if showFirst:
        print("Primeiro exercício:\n")
        firstExercise("first_input")
    # 2-)
    if showSecond:
        print("Segundo exercício: ")
        secondExercise("second_input")
    # 3-)
    if showThird:
        print("Terceiro exercício: ")
        thirdExercise("third_input")
main(False, True, True)
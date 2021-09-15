import random
import os
import numpy as np




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
    # A NASA finalmente anunciou a descoberta de vida fora da Terra. Uma sonda enviada à Marte detectou diversas
    # formas de vida, e coletou indivíduos, que foram trazidos de volta a nosso planeta.
    # Internamente, esses indivíduos alienígenas são bem diferentes das formas de vida terrestres. Enquanto que, por
    # aqui, a ordem das bases no DNA determina as características do indivíduo, nos marcianos só importa quantas cópias
    # de cada base estão presentes.
    # Mais especificamente, o “mDNA” (ou DNA marciano) é composto de 15 bases, representadas pelas letras de A a O.
    # Uma espécie é unicamente determinada pela quantidade de cada uma dessas bases que aparece em seu mDNA. Dois
    # indivíduos de uma mesma espécie podem ter sequências de mDNA distintas. Por exemplo, um indivíduo com
    # mDNA AABABJJ é da mesma espécie que um indivíduo com mDNA AJBAJBA, pois ambos possuem três bases A,
    # duas bases B e duas bases J. Indivíduos ABACA e ABABCA, porém são de espécies diferentes: enquanto o primeiro
    # possui apenas uma base B, o segundo possui duas cópias dessa base.
    # São dadas as sequências de mDNA de n indivíduos. Determine quantas espécies distintas estão presentes.
    # Entrada:
    #   A entrada possui vários casos de teste. Cada caso de teste começa com um inteiro n, que representa o número de
    #   indivíduos (0 < n < 65536). Em seguida há n linhas, cada uma das quais com a descrição do mDNA de um indivíduo.
    #   Essa descrição é composta apenas por letras maiúsculas entre A e O (inclusive), e possui no máximo 100 caracteres.
    #   A entrada termina com n=0, que não deve ser processado.
    if not os.path.exists(fileDir): os.makedirs(fileDir)
    def generateInput(path):
        possibleLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        file = open(path, "w+", encoding="UTF-8")
        nChoice = np.arange(0, 65536)
        for i in nChoice:
            file.write(str(i) + "\n")
            nChar = random.randint(0, 100)
            for j in range(i):
                output = ""
                for i in range(nChar):
                    nList = random.randint(0, len(possibleLetters)-1)
                    output += possibleLetters[nList]
                file.write(output)
                file.write("\n")
        file.close()
    generateInput(f"{fileDir}/alien.txt")
def thirdExercise(fileDir):
    # vai ser realizada a sensacional final mundial da fórmula 1. Os competidores se alinham na largada e
    # disputam a corrida. Você vai ter acesso aos grids de largada e de chegada. A questão é determinar o número
    # mínimo de ultrapassagens que foram efetuadas durante a competição.
    # Entrada
    # Cada caso de teste utiliza três linhas. A primeira linha de um caso de teste contém um inteiro N (2 ≤ N ≤ 24)
    # indicando o número de competidores. Cada competidor é identificado com um número de 1 a N. A segunda
    # linha de cada caso tem os N competidores, em ordem do grid de largada. A terceira linha de cada caso tem
    # os mesmos competidores, porém agora na ordem de chegada.
    # Saída
    # Para cada caso de teste imprima uma linha contendo um único número inteiro, que indica o número mínimo
    # de ultrapassagens necessárias para se chegar do grid de largada ao grid de chegada
    if not os.path.exists(fileDir): os.makedirs(fileDir)
    


# Para habilitar o exercício, só alterar o valor do parâmetor do mesmo para True
def main(showFirst = False, showSecond = False, showThird = False):
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
main(showFirst = False, showSecond = True, showThird = True)
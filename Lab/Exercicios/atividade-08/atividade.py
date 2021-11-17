# 3 listas: grupo1, grupo2, grupo1+grupo2. Encontrar elemento de acordo com o atributo do input
class Person():
    def __init__(self, name, index, qty):
        self.name = name
        self.index = index
        self.qty = qty
    def __str__(self):
        return (f"Nome: {self.name}, Index: {self.index}, Quantidade: {self.qty}")

def readFile(filename):
    content = []
    file = open(filename, "r+", encoding = "UTF-8")
    for line in file:
        content.append(line.rstrip().replace("\t", ""))
    file.close()
    return content
def filterList(aList):
    filtered = []
    for content in aList:
        atributes = content.split(";")
        person = Person(atributes[0], atributes[1], atributes[2])
        filtered.append(person)
    return filtered
def createGroup(groupName):
    rawFile = readFile(groupName)
    group = filterList(rawFile)
    return group
def binarySearch(aList, item, atributeAsString):
    low = 0
    high = len(aList) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if getattr(aList[mid], atributeAsString) < item:
            low = mid + 1
        elif getattr(aList[mid], atributeAsString) > item:
            high = mid - 1
        else:
            return mid
    return -1
def printGroup(group):
    i = 0
    for person in group:
        print(f"{i} -> {person}")
        i += 1

def searchName(group, name, atributeAsString, showSortedGroup = False):
    atributeAsString = atributeAsString.lower()
    group.sort(key=lambda x: getattr(x, atributeAsString))
    if showSortedGroup:
        print(f"Grupo ordenado por: {atributeAsString}")
        printGroup(group)
    return binarySearch(group, name, atributeAsString)



def main():
    groupOne = createGroup("grupo1.txt")
    groupTwo = createGroup("grupo2.txt")
    groupThree = groupOne + groupTwo
    atribute = int(input("Você quer procurar por qual atributo?\n1 = Nome\n2 = Index\n3 = Quantidade\n"))
    if atribute == 1: atribute = "name"
    elif atribute == 1: atribute = "index"
    elif atribute == 2: atribute = "qty"
    else: raise Exception
    value = input("Você quer procurar qual valor?\n")
    showSortedGroup = input("Você quer ver a lista inteira? (S/N)\n")
    showSortedGroup = True if showSortedGroup.lower() == "s" else False
    result = searchName(groupThree, value, atribute, showSortedGroup)
    if result != -1:
        print(f"Atributo encontrado: Index = {result}")
    else: 
        print("Atributo não encontrado!")
main()
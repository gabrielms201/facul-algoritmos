def sortFile(file):
    # Instancia uma lista vazia
    content = []
    # Da append em cada linha nessa lista
    for line in file:
        content.append(line)
    # Verifica necessidade de adicionar quebra de linha no ultimo elemento da lista
    if content[-1][-1]!= "\n": content[-1] = content[-1] + "\n"
    # Aproveita função sort() para ordenar em ordem alfabética, sem criar a necessidade de desenvolver um algoritmo que faz essa função
    content.sort()
    return content
def main():
    file = open("times.txt","r",encoding="utf-8")
    sorted = sortFile(file)
    print("Times:")
    for words in sorted:
        print(words, end = "")
    file.close()
main()

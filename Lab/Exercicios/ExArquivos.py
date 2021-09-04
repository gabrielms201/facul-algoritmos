import random
import statistics as st
#1
def escrita(filename):
    file = open(filename, "w+")
    for i in range(10000):
        file.write(str(random.randrange(0, 10000)))
        file.write("\n")
    file.close()
#2
def leitura(filename):
    def adiciona(inicio, fim):
        file = open(filename, "r")
        lista = []
        for linha in file:
            if int(linha) in range (inicio,fim):
                lista.append(int(linha.rstrip()))
        lista.sort()
        file.close()
        return(lista)
    def armazena():
        i = 0
        j = 1000
        lista = []
        while j <= 10000:
            lista.append((adiciona(i, j)))
            i+= 1000
            j+= 1000
        for i in range(9):
            print(f"Lista {i}:\n{lista[i]}\n\n")
        return lista
    return armazena()
#3
def calcularListas(listas):
    for lista in listas:
        moda = st.mean(lista)
        media = st.mode(lista)
        mediana = st.median(lista)
        print(f"Dados da lista {listas.index(lista)}:\n\t->Moda: {moda:.2f}\n\t->Media: {media:.2f}\n\t->Mediana:{mediana:.2f}")
        
try:
    nomeArquivo = "output1.txt"
    escrita(nomeArquivo)
    listas = leitura(nomeArquivo)
    calcularListas(listas)
except Exception as e:
    print(f"Exceção capturada: {e}")
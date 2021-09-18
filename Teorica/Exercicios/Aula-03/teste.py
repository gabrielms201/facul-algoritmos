#Faça um programa que leia duas listas e que gere uma terceira lista com:
# 1- Os elementos das duas primeiras
# 2- Os elementos das duas primeiras intercalados
# 3- Sem elementos repetidos

import timeit
# Parte 1:
lista1 = [1,2,3,3]
lista2 = [4,5,6,6]
lista3 = lista1 + lista2 # 1
print(f"1-) {lista3}")

# Parte 2:
lista3 = []
for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(f"2-) {lista3}")
# Parte 3:
lista3 = []
achou = False
# Eu sei que isso poderia ser mais otimizado utilizando funções, mas deixei assim para refletir a explicação do professor...
def ex1(x):
    achou = False
    for i in range(len(lista2)):
        for j in range(len(lista3)):
            if lista1[i] == lista3[j]:
                achou = True
        if not achou:
            lista3.append(lista1[i])
        achou = False
        for j in range(len(lista3)):
            if lista2[i] == lista3[j]:
                achou = True
        if not achou:
            lista3.append(lista2[i])
        achou = False
    print(f"3- ){lista3}")
    return x
# Em função
lista3 = []
def ex2(x):
    def adiciona(listIn, listOut):
        achou = False
        for j in range(len(listOut)):
            if listIn[i] == listOut[j]:
                achou = True
        if not achou:
            listOut.append(listIn[i])
            achou = False
            
    for i in range(len(lista2)):
        adiciona(lista1, lista3)
        adiciona(lista2, lista3)
    print(f"Resultado mais otimizado, na minha visão: {lista3}")
    return x

def main():
    trials = 10_000_000
    kwargs = {"setup" : "x=42", "globals" : globals(), "number" : trials }

    one_time = timeit.timeit("ex1(x)", **kwargs)
    two_time = timeit.timeit("ex2(x)", **kwargs)

    print(f"{one_time:.02f}")
    print(f"{two_time:.02f}")
main()
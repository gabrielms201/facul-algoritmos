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
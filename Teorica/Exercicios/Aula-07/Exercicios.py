
def ex4():
    # 4.(RECURSÃO) Qual o valor que a função recursiva seguinte retorna, dado um argumento n inteiro positivo qualquer? 
    # def rfunc(n): 
    # 	if n == 0: 
    # 		return 0 
    # 	else: 
    # 		return rfunc(n - 1) + 2
    #         # Aqui, o resultado da primeira função, será baseado no valor que a funcao2 retornará + 2. 
    #         O procedimento ocorre até que seja acumulado a soma de 2 até o momento que o valor fique o dobro do original
    print("A função retorna o dobro do valor dado (valor da Caso seja maior que 0)")
    print("A recursão ocorre até o valor que é passado ser negativo, fazendo com que a soma com 2 faça com que o núemro fique, eventualmente, com o dobro de seu valor")
def ex5():
    # Implemente uma função iterativa e outra função recursiva que receba um número inteiro positivo na base decimal e o converta para a base binária.
    # Recursiva:
    def conversor(n):
        if n == 0: return 0
        return (n % 2 + 10 * (conversor( n // 2 )))
    print(conversor(50000000))
    # Iterativa:
    def conversorIterativo(n):
        resultado = ""
        while n > 0:
            resultado += str(n % 2)
            n = n // 2
        return int(resultado[::-1])
    print(conversorIterativo(50000000))
def ex6():	
# (ORDENAÇÃO) O algoritmo Bubble Sort é popular, mesmo que ineficiente. Usando-se esse algoritmo para ordenar uma tabela, alocada sequencialmente, em ordem crescente contendo os números [5, 4, 1, 3, 2] serão feitas:
# a)	10 comparações e 8 trocas 
# b)	10 comparações e 9 trocas 
# c)	10 comparações e 10 trocas 
# d)	16 comparações e 9 trocas
# e)	16 comparações e 10 trocas
    print("Resposta: (A)")
ex4()
ex5()
ex6()
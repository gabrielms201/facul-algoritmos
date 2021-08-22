# Ricardo Ruiz
# Aplicar um código funcional dentro de uma lista, onde vai imprimir 10k itens, sendo que se o índice for primo, será impresso "1". 
# Caso o contrário, "0"
def isPrime(number):
    for i in range(2, number):
        if number % i == 0: return False
    return False if number <= 1 else True
list = [i if isPrime(i) else 0 for i in range(0, 10000)]
print(list)



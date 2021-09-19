# 1.
#  > Anagrama é um jogo de palavras que utiliza a transposição ou rearranjo de letras de uma palavra ou frase, com o intuito de formar outras palavras com ou sem sentido.
#  > É calculado através da propriedade fundamental da contagem, utilizando o fatorial de um número de acordo com as condições impostas pelo problema. 
#  > Assim, vamos determinar os anagramas da palavra: ESCOLA

# A palavra possui 6 letras, dessa forma, basta determinarmos o valor de 6! (seis fatorial).
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

# a)	Implemente um programa recursivo para fazer o anagrama da palavra cat.
# b)	Implemente um programa recursivo para fazer o anagrama da palavra escola.
# c)	Você conseguiria implementar um programa “genérico” para calcular o anagrama de qualquer palavra?


def fatorial(num):
    fat = 1
    for i in range(num):
        fat = fat * num
        num -= 1
    return fat


def primeiro():
    palavra = "cat"
    anagramas = fatorial(len(palavra))
    print(anagramas)


def segundo():
    palavra = "escola"
    anagramas = fatorial(len(palavra))
    print(anagramas)

def terceiro():
    def gerarAnagrama(palavra):
        repetidas = [] ; letras = []
        for letra in palavra: 
            if palavra.count(letra) > 1 and letra not in letras:
                repetidas.append(palavra.count(letra))
                letras.append(letra)
        dividendo = fatorial(len(palavra))
        denominador = 1
        for e in repetidas: denominador += fatorial(e)
        anagramas = dividendo/denominador
        return anagramas   
    palavra = input("Digite a palabra para gerar o anagrama: ")
    print( gerarAnagrama(palavra) )
    
print("\nPrimeiro:")
primeiro()
print("\nSegundo: ")
segundo()
print("\nTerceiro:")
terceiro()
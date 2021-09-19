class Pessoa():
    def __init__(self, nome, indice, quantidade):
        self.nome = nome
        self.indice = indice
        self.quantidade = quantidade
    def __str__(self):
        return (f"Nome: {self.nome}\tIndice: {self.indice}\tQuantidade: {self.quantidade}")
class Lista():
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        self.lista = []
        self.pessoas = []
    def instanciarLista(self):
        arquivo = open(f"{self.nomeArquivo}.txt", "r+", encoding = "UTF-8")
        atributos = [linha.rstrip().replace("\t", "") for  linha in arquivo]
        arquivo.close()
        for e in atributos:
            atributos = e.split(";")
            nome = atributos[0]
            quantidade  = atributos[1]
            indice = atributos[2]
            pessoa = Pessoa(nome, indice, quantidade)
            self.pessoas.append(pessoa)
    def ordernarIndice(self):
        for i in range(len(self.pessoas) - 1, 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if self.pessoas[j].indice > self.pessoas[maxIndex].indice:
                    maxIndex = j
            self.pessoas[i], self.pessoas[maxIndex] = self.pessoas[maxIndex], self.pessoas[i]
        return self.pessoas
    def ordernarQuantidade(self):
        for i in range(len(self.pessoas) - 1, 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if self.pessoas[j].quantidade > self.pessoas[maxIndex].quantidade:
                    maxIndex = j
            self.pessoas[i], self.pessoas[maxIndex] = self.pessoas[maxIndex], self.pessoas[i]
        return self.pessoas
    def ordernarNome(self):
        for i in range(len(self.pessoas) - 1, 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if self.pessoas[j].nome > self.pessoas[maxIndex].nome:
                    maxIndex = j
            self.pessoas[i], self.pessoas[maxIndex] = self.pessoas[maxIndex], self.pessoas[i]
        return self.pessoas

lista = Lista("grupo1")
lista.instanciarLista()

print("Ordenado por Indice: ")
lista.ordernarIndice()
for pessoa in lista.pessoas: print(pessoa)
print("Ordenado por Quantidade: ")
lista.ordernarQuantidade()
for pessoa in lista.pessoas: print(pessoa)
print("Ordenado por Nome: ")
lista.ordernarNome()
for pessoa in lista.pessoas: print(pessoa)



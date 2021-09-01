# salas = [10,2,1,3,0]
# Possui a quantidade de lugares vagos nas salas: 1,2,3,4 e 5 respectivamente. 
# Seu programa deve solicitar ao cliente a Sala desajada, imprimir a quantidade de lugares vagos e perguntar quantos lugares serão ocupados. 
# Seu programa deverá validar se a quantidade solicitada para a sala é válida, caso positivo deve atualizar os lugares disponiveis da sala.
# Crei também um menu para controlar toda essa interação, tendo uma das opções a possibildade de listar as salas e sua ocupação

class Sala():
    def __init__(self, id, vagos):
        self.id = id
        self.vagos = vagos
        self.ocupados = []
    def ocupar(self, lugar):
        self.ocupados.append(lugar)
        self.vagos.remove(lugar)
    def __str__(self):
        return (f"Sala: {self.id}\nLugares Vagos: {self.vagos}\nLugares Ocupados: {self.ocupados}")

lugares = [1,2,3,4,5]
salas = [Sala(10, lugares), Sala(2, lugares), Sala(1, lugares), Sala(1, lugares), Sala(3, lugares), Sala(0, lugares)]  

def encontrarSala(salas, id):
    for e in salas:
        if e.id == id: return e
    return False
def menu():
    id = int(input("Digite a sala desejada: "))
    sala = encontrarSala(salas, id)
    print(f"Sala encontrada: {sala}")
    quantidade = int(input("Quantos lugares serão ocupados?"))
    if len(sala.vagos) >= quantidade:
        for i in range(quantidade):
            ocupar = int(input("Qual lugar deseja ocupar? "))
            sala.ocupar(ocupar)
        print(sala)
        menu()
    else:
        print("Não é possível ocupar, pois não há lugares vagos para a quantia desejada...") 
        menu()

menu()
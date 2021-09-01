from os import linesep as endl

# Ricardo Ruiz

file = open("arquivo.txt", "r", encoding = "utf-8")
# Obter linhas:
line = file.readline()
print(f"\nFirst Line: {line}")
line = file.readline()
print(f"Second Line: {line}")
# Acessar index da string da linha
line = file.readline()
print(line[0], endl)
# Percorrer linhas:
for line in file:
    print(line, end = "")


# Abre o arquivo
file = open("times.txt", "r", encoding = "utf-8")
# Main 
def main():
    output = []
    for line in file:
        output.append(line)
    print("\n>> Lista de jogos <<\n")
    for i in output:
        count = 1
        for j in range(len(output)):
            if count >= len(output)-output.index(i): 
                break
            print("» " + i.rstrip() + " x " + output[output.index(i)+count].rstrip())
            count += 1
        if count > len(output)+1: 
            break
main()
# Fecha o arquivo 
file.close()

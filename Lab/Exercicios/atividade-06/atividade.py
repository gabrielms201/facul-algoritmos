def primeiro():
    n = int( input("Digite o valor de N:") )
    def a(n):
        an = a0 = 1
        for i in range(n):
            an = 3*(an-1)
            n -= 1
        return an
    def b(n):
        an = a0 = 3
        for i in range(n):
            an = -2*(an-1)
            n -= 1
        return an
    def c(n):
        an = a1 = 0
        if n >= 2:
            for i in range(n): 
                an = (an-1) + (n-1)
                n -= 1
            return an
        else: return None
    def d(n):
        an = a0 = 1
        for i in range(n):
            an = (an-1) + 2**n
            n -= 1
        return an
    def e(n):
        an = a0 = 1
        for i in range(n):
            an = (an-1) + (2**(n-1))
            n -= 1
        return an
    def f(n):
        tn = t1 = 2
        for i in range(n):
            tn = 2 * tn*(n-1)
            n -= 1
        return tn
    print(f"a-) {a(n)}")
    print(f"b-) {b(n)}")
    print(f"c-) {c(n)}")
    print(f"d-) {d(n)}")
    print(f"e-) {e(n)}")
    print(f"f-) {f(n)}")

def segundo():
    valor = int(input("Digite o seu número em decimal: "))
    resto = valor % 2
    quociente = valor // 2
    destino = ""
    while quociente != 0:
        resto = valor % 2
        destino += str(resto)
        quociente = valor // 2
        valor = quociente
    print(destino[::-1])
primeiro()
print(segundo())
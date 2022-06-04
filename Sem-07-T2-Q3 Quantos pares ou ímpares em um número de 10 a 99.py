n = int(input())
cont = 0
if 10 <= n <= 99: 
    lista = [int(a) for a in str(n)]
    for impar in lista: 
        if impar % 2 != 0: 
            cont = cont + 1
    if cont == 1:
        print("Apenas um dígito é ímpar.")
    if cont == 0:
        print("Nenhum dígito é ímpar.")
    if cont == 2 :
        print("Os dois dígitos são ímpares.")

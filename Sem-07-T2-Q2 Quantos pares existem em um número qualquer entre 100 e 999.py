n = int(input())
cont = 0
if 100 <= n <= 999: 
    lista = [int(a) for a in str(n)]
    for par in lista: 
        if par % 2 == 0: 
            cont = cont + 1 
    print("{}".format(cont))
else:
    print(cont)

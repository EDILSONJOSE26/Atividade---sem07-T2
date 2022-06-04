s_nome = input().strip()
status_c = int(input())
if status_c == 1:
    x = input().strip()
    print(len(s_nome + x))
elif status_c == 2:
    print(len(s_nome))

else:
    print('erro')

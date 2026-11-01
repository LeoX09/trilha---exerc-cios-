entrada = input().split(" ")

lista = []

for item in entrada:
    lista.append(int(item))

lista_ortedenada = sorted(lista)

for i in range(len(lista_ortedenada)):
    print(lista_ortedenada[i])
    
print()

for j in range(len(lista)):
    print(lista[j])
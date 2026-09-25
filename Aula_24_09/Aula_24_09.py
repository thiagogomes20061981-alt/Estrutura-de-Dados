def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1
lista = [10, 20, 32, 40]
alvo = 32
busca_linear(lista, alvo) 

print(busca_linear(lista, alvo))

##################################################################################################


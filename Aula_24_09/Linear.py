def busca_linear(lista, alvo):
    for indice, valor in enumerate(lista):
        if valor == alvo:
            return indice
    return -1

# Lista original
lista = [40, 10, 70, 20, 60, 30, 50]

# Busca linear
alvo = 50
resultado = busca_linear(lista, alvo)

if resultado != -1:
    print(f"Elemento {alvo} encontrado no índice {resultado}.")
else:
    print(f"Elemento {alvo} não encontrado na lista.")

# Organizando a lista ao final do código
lista.sort()
print("Lista ordenada:", lista)
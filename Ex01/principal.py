class Node:
    def __init__(self, chamado):
        self.chamado = chamado
        self.next = None


class ListaChamados:
    def __init__(self):
        self.head = None

    def inserir_fim(self, chamado):
        novo = Node(chamado) #Torna o chamado em um nó

        # Se a lista estiver vazia
        if self.head is None:
            self.head = novo
            return

        # Percorre até o último nó
        atual = self.head

        while atual.next is not None:
            atual = atual.next

        # Liga o último nó ao novo
        atual.next = novo

    def exibir(self):
        atual = self.head

        # Fica colocando o chamado 0 na tela e vai para o próximo nó até chegar no final da lista
        while atual is not None:
            print(atual.chamado, end=" -> ")
            atual = atual.next

        # Quando chega no none, printa none
        print("None")

    def buscar(self, chamado):
        atual = self.head
        posicao = 0

        while atual is not None:
            if atual.chamado == chamado:
                return posicao # Fala para o codigo qual o numero do chamado que ele está

            atual = atual.next
            posicao += 1 # Adiciona 1 a posição para cada nó que ele passa para que o usuário saiba a posição do chamado

        return -1 # Subtrai um para o codigo saber que o chamado não foi encontrado na lista
    
lista = ListaChamados()

while True:
    chamado = input()

    # Quando digita fim ele para de coletar
    if chamado == "fim":
        break

    lista.inserir_fim(chamado)


lista.exibir()

procurado = input()

posicao = lista.buscar(procurado)

if posicao != -1:
    print(f"Chamado '{procurado}' encontrado na posição {posicao}.")
else:
    print(f"Chamado '{procurado}' não foi encontrado.")
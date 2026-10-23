"""Prática orientada: Árvore Binária de Busca (BST).

SUA MISSÃO: complete a função buscar (procure "MISSÃO" abaixo).
Antes de executar, faça os Exercícios 1 a 3 da folha no papel.
Depois execute e confira se o programa mostra o mesmo que você.

Regras da aula:
- Menor vai para a esquerda, maior vai para a direita.
- Valor repetido não entra.
- Para remover um nó com dois filhos, o menor valor da direita toma o lugar dele.

Execute:  python bst_completo.py
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    elif valor > raiz.valor:
        raiz.dir = inserir(raiz.dir, valor)
    return raiz  # valor repetido: nada muda


def buscar(raiz, valor):
    if raiz == None:
        return False

    if raiz.valor == valor:
        return True

    if valor < raiz.valor:
        return buscar(raiz.esq, valor)
    
    else:
        return buscar(raiz.dir, valor)
    
def em_ordem(raiz):
    if raiz is None:
        return []
    return em_ordem(raiz.esq) + [raiz.valor] + em_ordem(raiz.dir)


def pre_ordem(raiz):
    if raiz is None:
        return []
    return [raiz.valor] + pre_ordem(raiz.esq) + pre_ordem(raiz.dir)


def pos_ordem(raiz):
    if raiz is None:
        return []
    return pos_ordem(raiz.esq) + pos_ordem(raiz.dir) + [raiz.valor]


def remover(raiz, valor):
    if raiz is None:
        return None
    if valor < raiz.valor:
        raiz.esq = remover(raiz.esq, valor)
    elif valor > raiz.valor:
        raiz.dir = remover(raiz.dir, valor)
    else:
        if raiz.esq is None:      # folha ou só filho direito
            return raiz.dir
        if raiz.dir is None:      # só filho esquerdo
            return raiz.esq
        menor = raiz.dir          # dois filhos: menor valor da direita
        while menor.esq is not None:
            menor = menor.esq
        raiz.valor = menor.valor
        raiz.dir = remover(raiz.dir, menor.valor)
    return raiz


def mostrar(raiz, espaco=""):
    """Desenha a árvore deitada: a direita fica em cima, a esquerda embaixo."""
    if raiz is None:
        return
    mostrar(raiz.dir, espaco + "      ")
    print(espaco + str(raiz.valor))
    mostrar(raiz.esq, espaco + "      ")


if __name__ == "__main__":
    raiz = None
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        raiz = inserir(raiz, valor)

    print("Árvore (vire a cabeça para a esquerda):")
    mostrar(raiz)
    print("\nPré-ordem:", pre_ordem(raiz))
    print("Em-ordem: ", em_ordem(raiz))
    print("Pós-ordem:", pos_ordem(raiz))

    print("\nConferindo buscar:")
    for valor, esperado in [(40, True), (60, True), (45, False), (100, False)]:
        resultado = buscar(raiz, valor)
        print(f"  buscar({valor}) = {resultado}  ->", "OK" if resultado == esperado else "ERRO")

    for valor in [20, 30, 50]:
        raiz = remover(raiz, valor)
        print(f"\nDepois de remover {valor}:")
        mostrar(raiz)
        print("Em-ordem:", em_ordem(raiz))

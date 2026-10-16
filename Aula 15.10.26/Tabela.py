class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = []
        for i in range(self.tamanho):
            self.tabela.append([])

    def funcao_hash(self, ra):
        return ra % self.tamanho

    def inserir(self, ra, nome):
        posicao = self.funcao_hash(ra)
        self.tabela[posicao].append([ra, nome])

    def buscar(self, ra):
        posicao = self.funcao_hash(ra)
        for aluno in self.tabela[posicao]:
            if aluno[0] == ra:
                return aluno[1]
        return None

    def exibir(self):
        for i in range(self.tamanho):
            if len(self.tabela[i]) == 0:
                print(f"Posicao {i}: (vazia)")
            else:
                itens = []
                for aluno in self.tabela[i]:
                    itens.append(f"{aluno[0]}-{aluno[1]}")
                print(f"Posicao {i}: " + ", ".join(itens))

    def contar(self):
        total = 0
        for lista in self.tabela:
            total += len(lista)
        return total

t = TabelaHash()
print(t.tabela)            # [[], [], [], [], []]
print(t.funcao_hash(412))  # 2
print(t.funcao_hash(520))  # 0

t.inserir(101, "Lucas")
t.inserir(207, "Marina")
t.inserir(315, "Pedro")
t.inserir(412, "Julia")
t.inserir(520, "Rafael")
print(t.tabela[2])   # [[207, 'Marina'], [412, 'Julia']]

print(t.buscar(520))   # Rafael
print(t.buscar(105))   # None

print(t.contar())          # 5
t.inserir(625, "Sofia")
print(t.contar())          # 6
t.exibir()
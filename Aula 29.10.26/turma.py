class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.lista = []
        for i in range(self.tamanho):
            self.lista.append([])

    def funcao_hash(self, matricula):
        return matricula % self.tamanho

    def inserir(self, matricula, nome):
        pos = self.funcao_hash(matricula)
        self.lista[pos].append([matricula, nome])

    def buscar(self, matricula):
        pos = self.funcao_hash(matricula)
        for item in self.lista[pos]:
            if item[0] == matricula:
                return item[1]
        return None

    def exibir(self):
        for i in range(self.tamanho):
            if len(self.lista[i]) == 0:
                print(f"[{i}] vazia")
            else:
                partes = []
                for item in self.lista[i]:
                    partes.append(f"{item[0]}-{item[1]}")
                print(f"[{i}] " + " -> ".join(partes))
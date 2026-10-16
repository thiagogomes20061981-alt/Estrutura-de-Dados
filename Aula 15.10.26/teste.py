from Tabela import TabelaHash

t = TabelaHash()
print(t.tabela)

t.inserir(101, "Lucas")
t.inserir(207, "Marina")
t.inserir(315, "Pedro")
t.inserir(412, "Julia")
t.inserir(520, "Rafael")

print(t.funcao_hash(412))
print(t.tabela[2])
print(t.buscar(520))
print(t.buscar(105))
t.exibir()

print(t.contar())
t.inserir(625, "Sofia")
print(t.contar())
t.exibir()
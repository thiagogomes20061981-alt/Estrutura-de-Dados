from Tabela import TabelaHash

t = TabelaHash()

# (a) e (b): ler e cadastrar até digitar "fim"
while True:
    entrada = input("RA (ou 'fim'): ")
    if entrada == "fim":
        break
    ra = int(entrada)
    nome = input("Nome: ")
    t.inserir(ra, nome)

# (c): exibir a tabela
t.exibir()

# (d): buscar
ra_busca = int(input("RA para buscar: "))
nome = t.buscar(ra_busca)
if nome is not None:
    print("Aluno encontrado:", nome)
else:
    print("RA nao cadastrado.")
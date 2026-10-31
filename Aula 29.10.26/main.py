from turma import TabelaHash

tabela = TabelaHash()

while True:
    matricula = input("Matricula (ou 'fim' para encerrar): ")
    if matricula == "fim":
        break
    nome = input("Nome: ")
    tabela.inserir(int(matricula), nome)

tabela.exibir()

busca = int(input("Digite a matricula para buscar: "))
nome_encontrado = tabela.buscar(busca)
pos = tabela.funcao_hash(busca)

if nome_encontrado is not None:
    print(f"Aluno {busca} encontrado: {nome_encontrado} (posicao {pos} da tabela).")
else:
    print(f"Aluno {busca} nao encontrado.")
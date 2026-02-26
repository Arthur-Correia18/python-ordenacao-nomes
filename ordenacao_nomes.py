# Programa: Ordenação de nomes em ordem alfabética
# Autor: Arthur 
# Descrição: Recebe uma lista de nomes e exibe em ordem alfabética

# Criando uma lista vazia para armazenar os nomes
nomes = []

# Solicitando a quantidade de alunos
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Laço de repetição para receber os nomes
for i in range(quantidade):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomes.append(nome)

# Ordenando a lista em ordem alfabética
nomes.sort()

# Exibindo os nomes ordenados
print("\nLista de alunos em ordem alfabética:")
for nome in nomes:
    print(nome)
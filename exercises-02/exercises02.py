# Exercícios de Entrada e Saída de Dados


# Exercício 2.1: faça um programa que receba um nome e imprima o mesmo
#   na vertical em escada invertida
def print_vertical_name(word):
    for i in range(len(word)):
        for j in range(len(word) - i):
            print(word[j], end="")
        print()


if __name__ == "__main__":
    name = input("Digite uma nome: ")
    print_vertical_name(name)

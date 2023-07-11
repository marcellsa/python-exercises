# Exercício 1: Crie uma função que receba dois números e retorne o maior deles
def find_max_number(number1, number2):
    """Calcule o maior valor entre os números"""
    return max(number1, number2)


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def arithmetic_average(list):
    """Calcule a média aritmética dos valores contidos na lista"""
    return sum(list) / len(list)


# Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
def write_number(n=2):
    """Imprima um quadradod e asteriscos"""
    rows = "*" * n
    return (rows + "\n") * n


print(arithmetic_average([3, 3, 3]))
print(write_number(5))

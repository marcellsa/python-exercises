# Exercício 1: Crie uma função que receba dois números e retorne o maior deles
def find_max_number(number1, number2):
    """Calcula o maior valor entre dois números"""
    # if number2 > number1:
    #     return number2
    # return number1
    return max(number1, number2)


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def arithmetic_average(list):
    """Calcula a média aritmética dos valores contidos numa lista"""
    # sum = 0
    # for number in list:
    #     total += number
    # return sum / len(list)
    return sum(list) / len(list)


# Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
def draw_square(n=2):
    """Imprime um quadradado feito de asteriscos"""
    for row in range(n):
        print("*" * n)


# Exercício 4: Crie uma função que receba uma lista de nomes
# e retorne o nome com a maior quantidade de caracteres.
def find_biggest_name(names):
    """Retorna elemento que contem o maior número de caracteres
    numa lista de nomes"""
    # biggest_name = ""
    # for name in names:
    #     if len(name) > len(biggest_name):
    #         biggest_name = name
    # return biggest_name
    return max(names)


# Exercício 5: Considere que a cobertura de tinta de 1 litro para cada
# 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custa R$ 80,00.
# Crie uam função que retorne dois valores em uma tupla
# contento a quantidade de latas de titnta a serem compradas
# e o preço total a partir do tamanho de uma parede em m2.
def paint_costs(area):
    """Calcula a quantidade necessária de latas de tinta e o custo total para
    pintar uma determinda área com base em uma quantidade de litros por área
    e no preço de cada lata de tinta"""
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    # Se houver um restnte, inscrementa o número de latas necessároas em 1.
    # Isso ocorre porque não podemos comoprar uma fração de lata de tinta,
    # então precisamos arredondar para cima se houver restante.
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price
    # outra alternativa pdoeria ser:
    # import math
    # ...
    # can_price = 80
    # required_casn = math.ceil(required_liters / 18)
    # return required_cans, required_cans * can_price


print(find_max_number(983, 1875))
print(arithmetic_average([1, 2, 3, 4]))
print(draw_square(6))
print(find_biggest_name(["Taina", "Marcel"]))

"""
POO Trybe
Exercício 2.2: Implementar uma classe Estatistica
Ela deve possui um atributo number (uma lista de números) com três métodos:
- um que calcula a média
- um que clacula a mediana
- e outro que calcula a moda de uam lista de números
"""
from collections import Counter


class Estatistica():
    def __init__(self, numbers):
        self.numbers = numbers

    def media(self):
        """Retorna o cálculo da média da lista de números"""
        return sum(self.number) / len(self.numbers)

    def mediana(self):
        """Retorna o cálculo da mediana da lista de números"""
        numbers = sorted(self.numbers)
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index] / 2)

    def moda(self):
        """Retorna a moda da lista de números"""
        number_most_common, _ = Counter(self.numbers).most_common()[0]
        return number_most_common
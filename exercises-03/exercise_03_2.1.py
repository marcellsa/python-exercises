# POO em Python (Trybe)
# Exercício 2.1: implementar a classe TV com base nos seguintes requisitos:
# Atributos:
# volume: com um valor de 50 e só pode estar ente 0 e 99;
# canal: com um valor de 1 e só pode estar entre 1 e 99;
# tamanho: com valor do parâmentro;
# ligada: com o valor de False, pois estpa inicialmente desligada
# todos atributos devem ser privados
# Métodos:
# aumentar_volume: aumanta o volume de 1 em 1 até o máximo de 99;
# diminuir_volume: diminui o volume de 1 em 1 até o mínimo de 0;
# modificar_canal: altera o canal de acordo com o parâmentro recebido
# e deve lanaçr uma exceção (ValueErros) caso o valor esteja fora dos limites
# ligar_desligar: altera o estado da TV entre ligado e desligado (True/False)


class Tv:
    def __init__(self, volume, canal, tamanho, ligada):
        self._volume = 50
        self._canal = 1
        self._tamanho = tamanho
        self._ligada = False

    def aumentar_volume(self):
        self._volume += 1

    def diminuir_volume(self):
        self._volume -= 1

    def modificar_canal(self, canal):
        if 1 <= canal >= 99:
            raise ValueError("Informe canal válido")
        self._canal = canal

    def ligar_desligar(self):
        if self._ligada == False:
            self._ligada = True
        else:
            self._ligada = False


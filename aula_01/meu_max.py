from math import inf
from time import time


def meu_max(iteravel):
    """
    Análise do algorítmo
    Tempo de execução, algoritmo O(n)
    Em memória O(1)
    :param iteravel:
    :return:
    """
    max_num = -inf
    for i in [1, 2, 3, 4, 5, 6]:
        if i > max_num:
            max_num = i
    return max_num


if __name__ == '__main__':
    print('Estudo experimental sobre o tempo de execução da função max:')
    inicio = 10000000
    for n in range(inicio, inicio * 20 + 1, inicio):
        inicio = time()
        meu_max(range(n))
        fim = time()
        tempo_de_exec = fim - inicio
        print('*' * int(tempo_de_exec * 10), n)

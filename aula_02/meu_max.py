from time import time
from math import inf


def meu_max(iteravel):
    """
    Análise do algorítmo
    Tempo de execução O(n)
    Uso de memória O(1)
    :param iteravel: list: int
    :return: int
    """
    num_max = -inf
    for iterado in iteravel:
        if iterado > num_max:
            num_max = iterado
    return num_max


if __name__ == '__main__':
    inicio = 10000000
    for n in range(0, inicio * 20 + 1, inicio):
        # Interval (0, n-1)
        interval = range(n)
        init = time()
        meu_max(interval)
        fim = time()
        temp_exec = fim - init
        print("*" * int(temp_exec*10), n)

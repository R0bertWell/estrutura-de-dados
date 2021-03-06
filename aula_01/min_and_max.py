from math import inf
from time import time


def min_and_max(lista: list[int], minimum=inf, maximum=-inf) -> tuple:
    if not lista or lista == []:
        raise ValueError
    for i in lista:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum


def min_and_max_recursive(iteravel):
    """
    Time complexity:
    Indice do iteravel = O(1)
    Percorrer por indices do iteravel = O(n)
    If's = O(1)
    Atribuições = O(1)

    Big O = O(n)

    :param iteravel:
    :return:
    """
    return _min_and_max_recursive(iteravel)


def _min_and_max_recursive(iteravel, pos=0, minimum=inf, maximum=-inf):
    if pos == len(iteravel):
        if minimum == inf and maximum == -inf:
            return ()
        return minimum, maximum
    if iteravel[pos] < minimum:
        minimum = iteravel[pos]
    if iteravel[pos] > maximum:
        maximum = iteravel[pos]
    return _min_and_max_recursive(iteravel, pos + 1, minimum, maximum)


if __name__ == '__main__':
    print(min_and_max([]))
    """inicio = 10000000
    for n in range(0, inicio * 20 + 1, inicio):
        # Interval (0, n-1)
        interval = range(n)
        init = time()
        min_and_max(interval)
        fim = time()
        temp_exec = fim - init
        print("*" * int(temp_exec * 10), n)"""

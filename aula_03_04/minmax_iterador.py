from collections import Iterable
from math import inf
from numbers import Number
from typing import Tuple


def _min_max_recursive(iterador, minimum, maximum):
    try:
        elemento = next(iterador)
    except StopIteration:
        return minimum, maximum
    else:
        if elemento < minimum:
            minimum = elemento
        if elemento > maximum:
            maximum = elemento
    return _min_max_recursive(iterador, minimum, maximum)


def minmax(iteravel: Iterable) -> Tuple[Number, Number]:
    """
    >>> minmax([])
    Traceback (most recent call last):
        ...
    ValueError: não existe mínimo e máximo de iterável sem elemento
    >>> minmax([1])
    (1, 1)
    >>> minmax(range(900))
    (0, 899)
    >>> minmax(i for i in range(5))
    (0, 4)


    :param iteravel:
    :return:
    """
    iterador = iter(iteravel)
    minimun, _ = _min_max_recursive(iterador, inf, -inf)
    if minimun is inf:
        raise ValueError('não existe mínimo e máximo de iterável sem elemento')
    # return () if minimun == inf else (minimun, _)
    return minimun, _

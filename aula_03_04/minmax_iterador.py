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
    ()
    >>> minmax([1])
    (1, 1)

    :param iteravel:
    :return:
    """
    iterador = iter(iteravel)
    minimun, _ = _min_max_recursive(iterador, inf, -inf)
    return () if minimun == inf else (minimun, _)

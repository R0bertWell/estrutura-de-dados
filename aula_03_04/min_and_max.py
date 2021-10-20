from cmath import inf


def min_and_max_iterativo_1(lista: list) -> tuple:
    """
    4 Atribuições, 2 comparações e 1 return = 4 + 2 + 1
    n = len(lista)
    For in n = O(n)
    O notation -> = 4 + 2 + 1 n
    O(4 + 2 + 1 + n )
    O(n) Em tempo de execução

    Em memória
    3 váriaveis fixas (min, max e i) = 3
    O(1) Constante em memória
    :param lista: list[int]
    :return: tuple(int, int) or () case n = 0
    """
    minimum = +inf
    maximum = -inf
    for i in lista:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return () if minimum == +inf else (minimum, maximum)

def min_and_max_iterativo_2(lista: list) -> tuple:
    """
    4 Atribuições, 2 comparações e 1 return = 4 + 2 + 1
    n = len(lista)
    For in n = O(n)
    O notation -> = 4 + 2 + 1 n
    O(4 + 2 + 1 + n )
    O(n) Em tempo de execução

    Em memória
    3 váriaveis fixas (min, max e i) = 3
    O(1) Constante em memória
    :param lista: list[int]
    :return: tuple(int, int) or () case n = 0
    """
    if not lista:
        return ()
    minimum = +inf
    maximum = -inf
    for i in lista:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return minimum, maximum


def _min_and_max_recursive(lista, minimum, maximum, length):
    """
   3/2 Comparações
   2 Atribuiçoes
   n Retornos ( Regidos pelo Length - 1)
   seria O(n *( 2 + 2 ) ) -> O(n)
   Time complexity = O(n)

   Em Space complexity é O(1), constante pois as variaveis sempre são as mesmas, fixas, muudando apenas seus valores
   :param lista: lista[int]
   :param minimum: int +inf
   :param maximum: int -inf
   :param length: len(lista)
   :return: tuple(int(minimum), int(maximum))
   """
    maximum = max(lista[length], maximum)
    minimum = min(lista[length], minimum)
    # if lista[length] > maximum:
    #     maximum = lista[length]
    # if lista[length] < minimum:
    #     minimum = lista[length]
    if length == 0:
        return minimum, maximum
    return _min_and_max_recursive(lista, minimum, maximum, length - 1)


def min_and_max_recursive(lista: list) -> tuple:
    length = len(lista)
    if length == 0:
        return ()
    return _min_and_max_recursive(lista, float('+inf'), float('-inf'), length - 1)


if __name__ == '__main__':
    print("MIN and MAX ITERATIVO1")
    print(min_and_max_iterativo_1([10, 2, 410, 11, -2, -50, 1000]))
    print(min_and_max_iterativo_1([1, -1, 0, 10]))
    print(min_and_max_iterativo_1([]))
    print("MIN and MAX ITERATIVO2")
    print(min_and_max_iterativo_2([10, 2, 410, 11, -2, -50, 1000]))
    print(min_and_max_iterativo_2([1, -1, 0, 10]))
    print(min_and_max_iterativo_2([]))
    print("MIN and MAX RECURSIVO")
    print(min_and_max_recursive([-1000.5, -100, 10000, 2, 410, 11, -2, -50, 1000]))
    print(min_and_max_recursive([1, -1, 0, 10]))
    print(min_and_max_recursive([]))

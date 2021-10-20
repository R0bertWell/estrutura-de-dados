def potencia_de_expoente_recursiva_linear(base: int, expoente: int):
    if expoente == 0:
        return 1
    return base * potencia_de_expoente_recursiva_linear(base, expoente - 1)


def _potencia_de_expoente_recursiva_linear_better(base: int, expoente: int, result: int):
    if expoente == 0:
        return result
    return _potencia_de_expoente_recursiva_linear_better(base, expoente - 1, result * base)


def potencia_de_expoente_recursiva_linear_better(base: int, expoente: int):
    return _potencia_de_expoente_recursiva_linear_better(base, expoente, result=1)


def _potencia_de_expoente_recursiva_logaritmica(base: int, expoente: int, result: int):
    """
    base ** expoente = se expoente é par: base ** ( 2 * n ), onde n é expoente % 2 == 0
                       Simplificando (base * base) ** n

                       se expoente é impar: 2*n + 1 base == ( 2*n + 1)
                    base ** (2*n + 1) -> base * (base **(2 * n) = base * [(base*base)**n]

    O(log(n)) para tempo de execução
    O(log(n)) para memória
    :param base: int
    :param expoente: int+
    :param result: int
    :return: int+
    """
    if expoente == 0:
        return result
    if expoente % 2 == 0:
        return _potencia_de_expoente_recursiva_logaritmica(base * base, expoente//2, result)
    else:
        result *= base
        return _potencia_de_expoente_recursiva_logaritmica(base, expoente - 1, result)


def potencia_de_expoente_recursiva_logaritmica(base: int, expoente: int):
    return _potencia_de_expoente_recursiva_logaritmica(base, expoente, result=1)


def potencia_de_expoente_iterativa(base, expoente):
    result = 1
    for _ in range(expoente):
        result *= base
    return result


if __name__ == '__main__':
    print(potencia_de_expoente_recursiva_logaritmica(2, 2))
    # print(potencia_de_expoente_iterativa(2, 5))

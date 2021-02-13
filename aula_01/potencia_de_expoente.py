def potencia_de_expoente_1(base: int, expoente: int):
    """
    Usando própria operação do Python
    Acredito que o tempo de execução seja O(1)
    Uso de memória O(1)
    :param base: int
    :param expoente: int
    :return: int
    """
    return base**expoente


def potencia_de_expoente_2(base: int, expoente: int):
    """
    Usando FOR
    Tempo de Execução em O(n)
    Uso de memória O(1) I GUESS kkk
    :param base: int
    :param expoente: int
    :return: int
    """
    init = 1
    for _ in range(expoente):
        init *= base
    return init


def potencia_de_expoente_linear(base: int, expoente: int):
    """
    Usando recursividade
    Tempo de execução linear O(n)
    Uso de memória O(1) I GUESS KKK
    :param base: int
    :param expoente: int
    :return: int
    """
    if expoente == 1:
        return base
    return base * potencia_de_expoente_linear(base, expoente - 1)


def potencia_de_expoente_logaritmica(base: int, expoente: int, resultado=1):
    """
    [BETTER]
    Tempo de execução O(log n)
    Uso de memória O(log n)
    :param base: int
    :param expoente: int
    :param resultado: int
    :return: int
    """
    if expoente == 0:
        return resultado
    elif expoente == 1:
        return base*resultado
    if expoente % 2 == 0:
        return potencia_de_expoente_logaritmica(base*base, expoente//2, resultado)
    else:
        resultado *= base
        return potencia_de_expoente_logaritmica(base, expoente-1, resultado)


"""
Tests :
"""
if __name__ == '__main__':
    print(potencia_de_expoente_logaritmica(2, 10))

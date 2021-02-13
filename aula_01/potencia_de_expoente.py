def potencia_de_expoente_1(base: int, expoente: int):
    return base**expoente


def potencia_de_expoente_2(base: int, expoente: int):
    init = 1
    for _ in range(expoente):
        init *= base
    return init


def potencia_de_expoente_linear(base: int, expoente: int):
    if expoente == 1:
        return base
    return base * potencia_de_expoente_linear(base, expoente - 1)


def potencia_de_expoente_logaritmica(base: int, expoente: int, resultado=1):
    if expoente == 0:
        return resultado
    elif expoente == 1:
        return base*resultado
    if expoente % 2 == 0:
        return potencia_de_expoente_logaritmica(base*base, expoente//2, resultado)
    else:
        resultado *= base
        return potencia_de_expoente_logaritmica(base, expoente-1, resultado)


if __name__ == '__main__':
    print(potencia_de_expoente_logaritmica(2, 2))

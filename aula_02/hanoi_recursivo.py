def _hanoi_recursivo(num_of_discs, origem, destino, suporte):
    """
    f(n) = 1 + 2 * f(n-1)
    
    :param num_of_discs:
    :param origem:
    :param destino:
    :param suporte:
    :return:
    """
    if num_of_discs == 1:
        print(f'{origem} => {destino} : {num_of_discs}')
        return
    _hanoi_recursivo(num_of_discs - 1, origem, suporte, destino)
    print(f'{origem} => {destino} : {num_of_discs}')
    _hanoi_recursivo(num_of_discs - 1, suporte, destino, origem)


def hanoi_recursivo(num_of_discs):
    return _hanoi_recursivo(num_of_discs, origem="A", destino="B", suporte="C")


if __name__ == '__main__':
    for i in range(1, 8):
        print(f'### HANOI PARA {i} DISCOS ###')
        hanoi_recursivo(i)

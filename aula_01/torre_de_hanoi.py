def _torre_de_hanoi_recursivo(num_de_discos, origem, destino, auxiliar):
    if num_de_discos == 1:
        print(f'{origem} --> {destino} : {num_de_discos}')
        return " "
    _torre_de_hanoi_recursivo(num_de_discos - 1, origem, auxiliar, destino)
    print(f'{origem} --> {destino} : {num_de_discos}')
    _torre_de_hanoi_recursivo(num_de_discos - 1, auxiliar, destino, origem)


def torre_de_hanoi(num_de_discos: int):
    _torre_de_hanoi_recursivo(num_de_discos, origem='A', destino='B', auxiliar='C')


if __name__ == '__main__':
    for i in range(3,5):
        print("Número de peças = ", i)
        torre_de_hanoi(i)

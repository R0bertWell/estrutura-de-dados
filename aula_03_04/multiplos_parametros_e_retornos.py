def gerar_ponto():
    return 1, 2, 3


ponto = gerar_ponto()
print(type(ponto))
primeiro, *_ = ponto # desempacotamento
print(primeiro, _)


def argumentos_variaveis(*args):
    print(args)
    print(type(args))

argumentos_variaveis(1, 2)
argumentos_variaveis(*(1, 2))
argumentos_variaveis(*[1, 2])
argumentos_variaveis(*'ab')

for chave, valor in {'pt': 'Portugues', 'en': 'Ingles'}:
    print(chave, valor)
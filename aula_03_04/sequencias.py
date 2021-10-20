from itertools import cycle
from time import perf_counter_ns

#lista_de_numeros = list(range(10))

#for i in cycle([11, 12]):
#    id_final = id(lista_de_numeros)
#    inicio = perf_counter_ns()
#    lista_de_numeros.append(i)
#    delta = perf_counter_ns() - inicio
#    print('*' * int(delta/100))


# Sequência Mutável:

lista = list()
print('#### SOMA DE LISTAS')
print(id(lista))
lista = lista + [1, 3, -4]
print(id(lista))

# Sequências Imutáveis

tupla = (1, 3)
print(type(tupla))
print('#### SOMA DE TUPLAS')
print(id(tupla))
tupla += (4, 6)
print(id(tupla))

print('#### SOMA DE STRINGS')
a = 'Wellington'
print(id(a))
a += 'Roberto'
print(id(a))
a.replace('e', '0')
print(id(a))
print(a)

print('### Sorted de lista')
print(lista)
print(id(lista))
print(sorted(lista))
print(id(lista))
print(lista)

print('### Sort de lista')
print(lista)
print(id(lista))
print(lista.sort())
print(id(lista))
print(lista)

print('### Objeto imutável mutante')

tupla = (lista,)
print(tupla)
print(id(tupla))
print(id(tupla[0]))
lista.append(0)
print(tupla)
print(id(tupla[0]))

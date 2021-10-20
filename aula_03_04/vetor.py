from array import array

vetor = array('h', [1, 2, 3, 4, 5])

print(type(vetor))
print(vetor)
print(vetor[0], vetor[1])
vetor.append(2**15-1)
print(vetor[-1])

teste = "oi"
print(id(teste))
teste = "joao"
print(id(teste))
class Noh:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class ListaLigadaSimples:
    def __init__(self):
        self.count = 0
        self._noh_inicial:Noh = None

    def __len__(self):
        if self._noh_inicial is None:
            return 0
        return 1

    def __getitem__(self, indice):
        if self._noh_inicial is None:
            raise IndexError(f'Não existe valor para o índice: {indice}')
        return self._noh_inicial.valor

    def adicionar(self, valor):
        if Noh(valor).valor is None:
            noh = Noh(valor)
            self._noh_inicial = noh
        else:
            noh = Noh(valor)
            self._noh_inicial = noh.valor
            self._noh_inicial.proximo = noh.proximo


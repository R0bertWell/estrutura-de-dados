class Noh:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __iter__(self):
        noh_atual = self
        while noh_atual:
            yield noh_atual
            noh_atual = noh_atual.proximo


class ListaLigadaSimples:
    def __init__(self):
        self._noh_inicial = None

    def __len__(self):
        if self._noh_inicial is None:
            return 0
        for indice, _ in enumerate(self._noh_inicial, start=1):
            pass
        return indice

    def __getitem__(self, indice):
        if self._noh_inicial is None:
            raise IndexError(f'Não existe valor para o índice : {indice}')
        noh = self._noh_inicial
        for indice_noh, noh_atual in enumerate(noh):
            if indice == indice_noh:
                return noh_atual.valor
        raise IndexError('Índice procurado além dos limites da lista')

    def __iter__(self):
        for noh in self._noh_inicial:
            yield noh.valor

    def adicionar(self, valor, indice=None):
        if indice == 0:
            noh_inicial_anterior = self._noh_inicial
            self._noh_inicial = Noh(valor, noh_inicial_anterior)
            return
        elif indice is None:
            noh_final = Noh(valor)
            if self._noh_inicial is None:
                self._noh_inicial = noh_final
            else:
                anterior_ultimo_noh = self._noh_inicial
                while anterior_ultimo_noh.proximo is not None:
                    anterior_ultimo_noh = anterior_ultimo_noh.proximo
                anterior_ultimo_noh.proximo = noh_final
        else:
            for indice_noh_atual, noh_atual in enumerate(self._noh_inicial, start=1):
                if indice == indice_noh_atual:
                    noh_meio = Noh(valor, noh_atual.proximo)
                    noh_atual.proximo = noh_meio

    def remover(self, indice):
        if self._noh_inicial is None:
            raise IndexError('Índice fora do limite da lista atual')
        if indice == 0:
            self._noh_inicial = self._noh_inicial.proximo
            return
        for indice_atual, noh_atual in enumerate(self._noh_inicial, start=1):
            if indice == indice_atual:
                if noh_atual.proximo.proximo:
                    noh_atual.proximo = noh_atual.proximo.proximo
                else:
                    noh_atual.proximo = None

# Minha implementação de alguns métodos
# class ListaLigadaSimples:
#     def __init__(self):
#         self.tam = 0
#         self._noh_inicial = None
#
#     def __len__(self):
#         return self.tam
#
#     def __getitem__(self, indice):
#         if self._noh_inicial is None or indice > self.tam:
#             raise IndexError(f'Não existe valor para o índice : {indice}')
#         count = 0
#         noh = self._noh_inicial
#         while noh:
#             if indice == count:
#                 return noh.valor
#             noh = noh.proximo
#             count += 1
#
#     def adicionar(self, valor):
#         if self._noh_inicial is None:
#             self._noh_inicial = Noh(valor)
#         else:
#             noh_final = Noh(valor)
#             anterior_ultimo_noh = self._noh_inicial
#             while anterior_ultimo_noh.proximo is not None:
#                 anterior_ultimo_noh = anterior_ultimo_noh.proximo
#             anterior_ultimo_noh.proximo = noh_final
#         self.tam += 1

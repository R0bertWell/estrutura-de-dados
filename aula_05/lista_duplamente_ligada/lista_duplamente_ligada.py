class Noh:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

    def __iter__(self):
        if self.esquerdo is None:
            while self:
                yield self
                self = self.direito
        else:
            while self:
                yield self
                self = self.esquerdo


class Lista():
    def __init__(self, primeiro=None, ultimo=None, tam=0):
        self.tam = tam
        self.primeiro = primeiro
        self.ultimo = ultimo

    def __iter__(self):
        if self.primeiro:
            for noh in self.primeiro:
                yield noh.valor

    def __reversed__(self):
        if self.ultimo:
            for noh in self.ultimo:
                yield noh.valor

    def __getitem__(self, indice):
        if self.tam == 0:
            raise ListaVaziaErro
        for i, noh in enumerate(self.primeiro):
            if indice == i:
                return noh.valor

    def adicionar(self, valor):
        if self.tam == 0:
            self.primeiro = Noh(valor)
            self.ultimo = self.primeiro
        else:
            last_ultimo_esquerdo = self.ultimo
            ultimo = Noh(valor, last_ultimo_esquerdo)
            self.ultimo.direito = ultimo
            self.ultimo = ultimo
        self.tam += 1

    def adicionar_a_esquerda(self, valor):
        if self.tam == 0:
            self.primeiro = Noh(valor)
            self.ultimo = self.primeiro
        else:
            novo_primeiro = Noh(valor, None, self.primeiro)
            self.primeiro.esquerdo = novo_primeiro
            self.primeiro = novo_primeiro
        self.tam += 1

    def remover(self):
        if self.ultimo is None:
            raise ListaVaziaErro
        retorno = self.ultimo.valor
        if self.tam == 1:
            self.primeiro = None
            self.ultimo = None
        else:
            anterior_ultimo = self.ultimo.esquerdo
            anterior_ultimo.direito = None
            self.ultimo = anterior_ultimo
        self.tam -= 1
        return retorno

    def remover_a_esquerda(self):
        if self.tam == 0:
            raise ListaVaziaErro('Erro lista vazia')
        retorno = self.primeiro.valor
        if self.tam == 1:
            self.primeiro = None
            self.ultimo = None
        else:
            novo_primeiro = self.primeiro.direito
            novo_primeiro.esquerdo = None
            self.primeiro = novo_primeiro
        self.tam -= 1
        return retorno


class ListaVaziaErro(Exception):
    pass

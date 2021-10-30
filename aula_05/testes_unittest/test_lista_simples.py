import unittest


class Noh:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class TesteNoh(unittest.TestCase):
    def test_criacao_de_noh_com_multiplos_objetos(self):
        noh = Noh(1)
        self.assertEqual(1, noh.valor)
import unittest

from aula_05.lista_simples.lista_simples import Noh, ListaLigadaSimples
from aula_05.poo.orientacao_a_objetos import Carro


class TesteNoh(unittest.TestCase):
    def test_criacao_de_noh_com_multiplos_objetos(self):
        for objeto in (1, 'Renzo', Carro('Chevete')):
            with self.subTest(objeto):
                noh = Noh(objeto)
                self.assertEqual(objeto, noh.valor)

    def test_proximo_noh_sem_inicializacao(self):
        noh = Noh(1)
        self.assertIsNone(noh.proximo)

    def test_proximo_noh_com_inicializacao(self):
        proximo = Noh(2)
        noh = Noh(1, proximo=proximo)
        self.assertIs(proximo, noh.proximo)


class TestListaLigadaSimples(unittest.TestCase):
    def test_criacao(self):
        lista_ligada = ListaLigadaSimples()
        self.assertEqual(0, len(lista_ligada))
        self.assertIsNone(lista_ligada._noh_inicial)

    def test_adicao_de_valor_lista(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        self.assertEqual(1, len(lista_ligada))

    def test_acesso_primeiro_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        self.assertEqual(1, lista_ligada[0])

    def test_acesso_segundo_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        self.assertEqual(1, lista_ligada[0])
        self.assertEqual(2, lista_ligada[1])

    def test_acesso_lista_vazia(self):
        lista_ligada = ListaLigadaSimples()
        with self.assertRaises(IndexError):
            lista_ligada[0]
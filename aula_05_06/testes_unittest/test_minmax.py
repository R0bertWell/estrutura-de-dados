import unittest

from aula_03_04.minmax_iterador import minmax


class TestMinMax(unittest.TestCase):
    def test_min_max_lista_com_um_elemento(self):
        numero = minmax([1])
        self.assertEqual((1, 1), numero)

    def test_min_max_lista_vazia_sem_assertRaises(self):
        try:
            minmax([])
        except ValueError:
            print('Deu certo')
        else:
            raise AssertionError()

    def test_min_max_lista_vazia_com_assertRaises(self):
        with self.assertRaises(ValueError):
            minmax([])
            
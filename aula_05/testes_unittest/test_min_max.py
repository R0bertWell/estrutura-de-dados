import unittest


from aula_01.min_and_max import min_and_max


class TestMinMax(unittest.TestCase):
    def test_min_max_lista_com_um_elemento(self):
        resultado = min_and_max([1])
        self.assertEqual((1, 1), resultado)

    def test_min_max_lista_com_dois_elementos(self):
        resultado = min_and_max([1, 2])
        self.assertEqual((1, 2), resultado)

    def test_min_max_lista_vazia(self):
        with self.assertRaises(ValueError):
            min_and_max([])

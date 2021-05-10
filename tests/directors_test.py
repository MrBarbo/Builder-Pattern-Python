from codigo.napolitana_director import NapolitanaDirector
from codigo.cuatro_quesos_director import CuatroQuesosDirector
from codigo.muzzarella_director import MuzzarellaDirector
import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)


class ClassTest(unittest.TestCase):
    #Testea que el director de muzzarella cree una pizza muzzarella
    def test_MuzzarellaDirectorCreatesMuzzarellaPizza(self):
        pizza_test = MuzzarellaDirector.construct()
        self.assertEqual("Muzzarella", pizza_test.tipo)
    #Testea que el director de 4 quesos cree una pizza quesos
    def test_CuatroQuesosDirectorCreatesCuatroQuesosPizza(self):
        pizza_test = CuatroQuesosDirector.construct()
        self.assertEqual("4 quesos", pizza_test.tipo)
    #Testea que el director de napolitana cree una pizza napolitana
    def test_NapolitanaDirectorCreatesNapolitanaPizza(self):
        pizza_test = NapolitanaDirector.construct()
        self.assertEqual("Napolitana", pizza_test.tipo)


if __name__ == '__main__':
    unittest.main()

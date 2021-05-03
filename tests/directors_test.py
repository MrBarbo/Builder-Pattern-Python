import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.muzzarella_director import MuzzarellaDirector
from codigo.cuatro_quesos_director import CuatroQuesosDirector
from codigo.napolitana_director import NapolitanaDirector

class ClassTest(unittest.TestCase):
    def test_MuzzarellaDirectorCreatesMuzzarellaPizza(self):
        pizza_test = MuzzarellaDirector.construct()
        self.assertEqual("Muzzarella",pizza_test.tipo)

    def test_CuatroQuesosDirectorCreatesCuatroQuesosPizza(self):
        pizza_test = CuatroQuesosDirector.construct()
        self.assertEqual("4 quesos",pizza_test.tipo)

    def test_NapolitanaDirectorCreatesNapolitanaPizza(self):
        pizza_test= NapolitanaDirector.construct()
        self.assertEqual("Napolitana",pizza_test.tipo)


if __name__ == '__main__':
    unittest.main()
    


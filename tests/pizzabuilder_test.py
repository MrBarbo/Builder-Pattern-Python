from codigo.pizza_builder import PizzaBuilder
import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

#Tests orientados a la clase "PizzaBuilder"
class PizzaBuilderTest(unittest.TestCase):
    #Testea que las pizzas se creen con los datos correctos
    def test_PizzaBuilderClassCreatesCorrectType(self):
        test_builder = PizzaBuilder()
        test_builder.set_tipo_pizza("Tipo1")
        self.assertEqual("Tipo1", test_builder.get_result().tipo)

    def test_PizzaBuilderClassCreatesCorrectCheese(self):
        test_builder = PizzaBuilder()
        test_builder.set_queso("Queso1")
        self.assertEqual("Queso1", test_builder.get_result().queso)

    def test_PizzaBuilderClassCreatesCorrectTopping(self):
        test_builder = PizzaBuilder()
        test_builder.set_topping("Top1")
        self.assertEqual("Top1", test_builder.get_result().topping)

    def test_PizzaBuilderClassCreatesCorrectMass(self):
        test_builder = PizzaBuilder()
        test_builder.set_masa("Masa1")
        self.assertEqual("Masa1", test_builder.get_result().masa)

    #Testea el metodo "print_data" de la clase "Pizza"
    def test_PizzaPrintDataMethod(self):
        test_builder = PizzaBuilder()
        test_builder.set_tipo_pizza("Tipo1")
        test_builder.set_queso("Queso1")
        test_builder.set_topping("Top1")
        test_builder.set_masa("Masa1")
        self.assertEqual("Tipo: Tipo1 Queso: Queso1 Masa: Masa1 Topping: Top1",
                         test_builder.get_result().print_data())


if __name__ == '__main__':
    unittest.main()

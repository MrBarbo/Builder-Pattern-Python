"The Builder Class"
from codigo.builder_interface import PizzaBuilderInterface
from codigo.pizza import Pizza


class PizzaBuilder(PizzaBuilderInterface):
    "El constructor de las pizzas"

    def __init__(self):
        self.pizza = Pizza()

    def set_tipo_pizza(self, tipo):
        self.pizza.tipo = tipo
        return self

    def set_queso(self, queso):
        self.pizza.queso = queso
        return self

    def set_masa(self, masa):
        self.pizza.masa = masa
        return self

    def set_topping(self, topping):
        self.pizza.topping=topping
        return self

    def get_result(self):
        return self.pizza

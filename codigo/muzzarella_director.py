
from codigo.pizza_builder import PizzaBuilder

class MuzzarellaDirector:
    @staticmethod
    def construct():
        "Constructs and returns the final product"
        pizza_actual = PizzaBuilder()
        pizza_actual.set_tipo_pizza("Muzzarella")
        pizza_actual.set_masa("Comun")
        pizza_actual.set_queso("Muzzarella")
        pizza_actual.set_topping("Ninguno")
        return pizza_actual.get_result()


from codigo.pizza_builder import PizzaBuilder


class CuatroQuesosDirector:
    @staticmethod
    def construct():
        # Va a construir una pizza con argumentos preestablecidos
        pizza_actual = PizzaBuilder()
        pizza_actual.set_tipo_pizza("4 quesos")
        pizza_actual.set_masa("Comun")
        pizza_actual.set_queso("4 quesos")
        pizza_actual.set_topping("Aceituna Negra")
        return pizza_actual.get_result()

from codigo.pizza_builder import PizzaBuilder


class NapolitanaDirector:
    @staticmethod
    def construct():
        # Va a construir una pizza con argumentos preestablecidos
        pizza_actual = PizzaBuilder()
        pizza_actual.set_tipo_pizza("Napolitana")
        pizza_actual.set_masa("Comun")
        pizza_actual.set_queso("Muzzarella")
        pizza_actual.set_topping("Tomate")
        return pizza_actual.get_result()

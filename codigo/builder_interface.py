from abc import ABCMeta, abstractmethod


class PizzaBuilderInterface(metaclass=ABCMeta):
    "Interface de la pizza"

    @staticmethod
    @abstractmethod
    def set_tipo_pizza(pizza_type):
        "Tipo de pizza"

    @staticmethod
    @abstractmethod
    def set_queso(queso):
        "Tipo de queso"

    @staticmethod
    @abstractmethod
    def set_masa(masa):
        "Tipo de masa"

    @staticmethod
    @abstractmethod
    def set_topping(toppping):
        "Topping de la pizza"

    @staticmethod
    @abstractmethod
    def get_result():
        "Retorna el producto final"

from abc import ABCMeta, abstractmethod
# Las clases abstractas tienen que usar una metaclase ABCMeta
# ABCMeta metaclass provides a method called register method that can be invoked by its instance.


class PizzaBuilderInterface(metaclass=ABCMeta):
    "Interface de la pizza"
    #Declaramos los métodos base del constructor
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

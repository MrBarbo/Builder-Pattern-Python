
# Clase de cada pizza individual

class Pizza():
    # Esta es la clase de cada uno de los elementos de la lista
    def __init__(self):
        self.tipo = None
        self.queso = None
        self.masa = None
        self.topping = None

    # Este método crea un string con los datos de la pizza
    def print_data(self):
        impresion = ("Tipo: "+self.tipo+" Queso: "+self.queso +
                     " Masa: "+self.masa+" Topping: "+self.topping)
        return impresion

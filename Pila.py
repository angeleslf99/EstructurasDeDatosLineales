class pila:
    __Pila = []

    def __init__(self):
        self.__Pila = []

    def Insertar(self, elemento):
        self.__listaPila.append(elemento)

    def PilaVacia(self):
        if len(self.__listaPila) == 0:
            return True
        else:
            return False

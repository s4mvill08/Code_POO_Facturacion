class Cliente:
    DESCUENTOS = {"regular": 0.0, "vip": 0.10}

    def __init__(self, documento, nombre, tipo="regular"):
        tipo = tipo.lower()
        if tipo not in Cliente.DESCUENTOS:
            raise ValueError("El tipo de cliente debe ser 'regular' o 'vip'.")
        self.__documento = documento
        self.__nombre = nombre
        self.__tipo = tipo

    @property
    def documento(self):
        return self.__documento

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipo(self):
        return self.__tipo

    def calcular_descuento(self):
        return Cliente.DESCUENTOS[self.__tipo]
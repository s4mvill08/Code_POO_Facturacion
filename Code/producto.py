class PrecioInvalidoError(Exception):
    pass

class CantidadInvalidaError(Exception):
    pass

class StockInsuficienteError(Exception):
    pass

class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if precio < 0:
            raise PrecioInvalidoError("El precio no puede ser negativo.")
        if stock < 0:
            raise CantidadInvalidaError("El stock inicial no puede ser negativo.")
        self.__codigo: str = codigo
        self.__nombre: str = nombre
        self.__precio: float = precio
        self.__stock: int = stock
        
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def hay_stock(self, cantidad):
        return cantidad <= self.__stock

    def reducir_stock(self, cantidad):
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor que cero.")
        if not self.hay_stock(cantidad):
            raise StockInsuficienteError(
                f"Stock insuficiente de '{self.__nombre}': "
                f"pedido {cantidad}, disponible {self.__stock}."
            )
        self.__stock -= cantidad

    def aumentar_stock(self, cantidad):
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor que cero.")
        self.__stock += cantidad

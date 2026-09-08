class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, cantidad: int):
        self.__codigo: str = codigo
        self.__nombre: str = nombre
        self.__precio: float = precio
        self.cantidad: int = cantidad
        
    def get_codigo(self) -> str:
        return self.__codigo

    def get_nombre(self) -> str:
        return self.__nombre

    def get_precio(self) -> float:
        return self.__precio
    
    def set_precio(self, precio: float):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo")
            
    def cantidad_disponible(self, cantidad_solicitada):
        return self.cantidad >= cantidad_solicitada

    def reducir_cantidad(self, cantidad_solicitada):
        if self.cantidad_disponible(cantidad_solicitada):
            self.cantidad -= cantidad_solicitada
        else:
            print("Cantidad insuficiente")
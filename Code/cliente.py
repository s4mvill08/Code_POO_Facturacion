class Cliente:
    def __init__(self, nombre: str, tipo_cliente: str):
        self.__nombre: str = nombre
        self.__tipo_cliente: str = tipo_cliente
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_tipo_cliente(self) -> str:
        return self.__tipo_cliente
    
    def set_tipo_cliente(self, tipo_cliente: str):
        if tipo_cliente == "regular" or tipo_cliente == "vip":
            self.__tipo_cliente = tipo_cliente
        else:
            print("Tipo de cliente no válido")
            
    def obtener_descuento(self) -> float:
        if self.__tipo_cliente == "vip":
            return 0.15
        else:
            return 0.0
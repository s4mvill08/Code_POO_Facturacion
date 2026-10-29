from abc import ABC, abstractmethod

class PagoRechazadoError(Exception):
    pass

class MedioPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

    @abstractmethod
    def generar_comprobante(self, monto):
        pass

class Efectivo(MedioPago):
    def __init__(self, monto_entregado: float):
        self.__monto_entregado: float = monto_entregado

    def procesar_pago(self, monto):
        if self.__monto_entregado < monto:
            raise PagoRechazadoError("El efectivo entregado no cubre el total.")
        return True

    def generar_comprobante(self, monto):
        cambio = self.__monto_entregado - monto
        return (f"Pago en efectivo, Recibido: ${self.__monto_entregado:,.0f} "
                f" Cambio: ${cambio:,.0f}")

class Tarjeta(MedioPago):
    def __init__(self, numero: str, titular: str, cupo: float):
        self.__numero: str = numero
        self.__titular: str = titular
        self.__cupo: float = cupo

    def procesar_pago(self, monto):
        if monto > self.__cupo:
            raise PagoRechazadoError("La tarjeta no tiene cupo suficiente.")
        self.__cupo -= monto
        return True

    def generar_comprobante(self, monto):
        return (f"Pago con tarjeta {self.__numero[-4:]} "
                f" Titular: {self.__titular}")

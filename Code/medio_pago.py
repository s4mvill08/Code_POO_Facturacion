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
    def __init__(self, monto_entregado):
        self.__monto_entregado = monto_entregado

    def procesar_pago(self, monto):
        if self.__monto_entregado < monto:
            raise PagoRechazadoError("El efectivo entregado no cubre el total.")
        return True

    def generar_comprobante(self, monto):
        cambio = self.__monto_entregado - monto
        return (f"Pago en EFECTIVO | Recibido: ${self.__monto_entregado:,.0f} "
                f"| Cambio: ${cambio:,.0f}")


class Tarjeta(MedioPago):
    def __init__(self, numero, titular, cupo):
        self.__numero = numero
        self.__titular = titular
        self.__cupo = cupo

    def procesar_pago(self, monto):
        if monto > self.__cupo:
            raise PagoRechazadoError("La tarjeta no tiene cupo suficiente.")
        self.__cupo -= monto
        return True

    def generar_comprobante(self, monto):
        return (f"Pago con TARJETA ****{self.__numero[-4:]} "
                f"| Titular: {self.__titular}")

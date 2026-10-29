from cliente import Cliente
from medio_pago import MedioPago

class Factura:
    _consecutivo: int = 0

    def __init__(self, cliente: Cliente, medio_pago: MedioPago):
        Factura._consecutivo += 1
        self.__numero: int = Factura._consecutivo
        self.__cliente: Cliente = cliente
        self.__medio_pago: MedioPago = medio_pago
        self.__items: list[list] = []
        self.__pagada: bool = False

    @property
    def numero(self):
        return self.__numero

    def agregar_producto(self, producto, cantidad):
        if self.__pagada:
            raise ValueError("La factura ya fue cerrada.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        for item in self.__items:
            if item[0] is producto:
                if not producto.hay_stock(item[1] + cantidad):
                    raise ValueError(f"Stock insuficiente de '{producto.nombre}'.")
                item[1] += cantidad
                return

        if not producto.hay_stock(cantidad):
            raise ValueError(f"Stock insuficiente de '{producto.nombre}'.")
        self.__items.append([producto, cantidad])

    def calcular_subtotal(self):
        subtotal = 0
        for producto, cantidad in self.__items:
            subtotal += producto.precio * cantidad
        return subtotal

    def calcular_descuento(self):
        return self.calcular_subtotal() * self.__cliente.calcular_descuento()

    def calcular_total(self):
        return self.calcular_subtotal() - self.calcular_descuento()

    def cerrar_venta(self):
        """Cobra y, solo si el pago se aprueba, descuenta el stock."""
        if not self.__items:
            raise ValueError("La factura no tiene productos.")
        if self.__pagada:
            raise ValueError("La factura ya fue cerrada.")

        self.__medio_pago.procesar_pago(self.calcular_total())
        for producto, cantidad in self.__items:
            producto.reducir_stock(cantidad)
        self.__pagada = True

    def generar_resumen(self):
        lineas = [
            "=" * 46,
            f"FACTURA N° {self.__numero:04d}",
            f"Cliente: {self.__cliente.nombre} ({self.__cliente.tipo.upper()})",
            "-" * 46,
        ]
        for producto, cantidad in self.__items:
            lineas.append(f"{producto.nombre:<14} x{cantidad:<3} "
                          f"${producto.precio * cantidad:>12,.0f}")
        lineas += [
            "-" * 46,
            f"Subtotal:  ${self.calcular_subtotal():>12,.0f}",
            f"Descuento: ${self.calcular_descuento():>12,.0f}",
            f"TOTAL:     ${self.calcular_total():>12,.0f}",
            "-" * 46,
            self.__medio_pago.generar_comprobante(self.calcular_total()),
            "=" * 46,
        ]
        return "\n".join(lineas)

    def imprimir_resumen(self):
        print(self.generar_resumen())

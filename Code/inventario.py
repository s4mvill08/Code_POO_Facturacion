from producto import Producto
from cliente import Cliente

class RegistroDuplicadoError(Exception):
    pass

class Inventario:
    def __init__(self):
        self.__productos: list[Producto] = []
        self.__clientes: list[Cliente] = []

    def registrar_producto(self, producto):
        if self.buscar_producto(producto.codigo) is not None:
            raise RegistroDuplicadoError(
                f"Ya existe un producto con código {producto.codigo}.")
        self.__productos.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.__productos:
            if producto.codigo == codigo:
                return producto
        return None

    def reabastecer(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe el producto {codigo}.")
        producto.aumentar_stock(cantidad)

    def listar_productos(self):
        return list(self.__productos)

    def productos_bajo_stock(self, umbral=5):
        return [p for p in self.__productos if p.stock <= umbral]

    def valor_total_inventario(self):
        total = 0
        for p in self.__productos:
            total += p.precio * p.stock
        return total

    def registrar_cliente(self, cliente):
        if self.buscar_cliente(cliente.documento) is not None:
            raise RegistroDuplicadoError(
                f"Ya existe un cliente con documento {cliente.documento}.")
        self.__clientes.append(cliente)

    def buscar_cliente(self, documento):
        for cliente in self.__clientes:
            if cliente.documento == documento:
                return cliente
        return None

    def listar_clientes(self):
        return list(self.__clientes)

    def clientes_por_tipo(self, tipo):
        tipo = tipo.lower()
        return [c for c in self.__clientes if c.tipo == tipo]

    def generar_reporte(self):
        lineas = ["REPORTE DE INVENTARIO"]
        for p in self.__productos:
            lineas.append(f"{p.codigo} | {p.nombre:<12} | "
                          f"${p.precio:>9,.0f} | stock: {p.stock}")
        lineas.append(f"Valor total del inventario: ${self.valor_total_inventario():,.0f}")
        lineas.append(f"Clientes registrados: {len(self.__clientes)} "
                      f"(VIP: {len(self.clientes_por_tipo('vip'))}, "
                      f"Regular: {len(self.clientes_por_tipo('regular'))})")
<<<<<<< HEAD
        return "\n".join(lineas)
=======
        return "\n".join(lineas)
>>>>>>> ec20e549281aa0211b3a5203ef7fbece3133ad0a

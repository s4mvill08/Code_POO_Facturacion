from producto import Producto
from cliente import Cliente
from medio_pago import Efectivo, Tarjeta
from inventario import Inventario
from factura import Factura

def main():
    inventario = Inventario()
    inventario.registrar_producto(Producto("P-01", "Arroz 1kg", 4500, 50))
    inventario.registrar_producto(Producto("P-02", "Aceite 1L", 12000, 20))
    inventario.registrar_producto(Producto("P-03", "Café 500g", 18000, 3))

    inventario.registrar_cliente(Cliente("1001", "Elena Rojas", "regular"))
    inventario.registrar_cliente(Cliente("1002", "Pedro Navas", "vip"))

    cliente = inventario.buscar_cliente("1002")
    factura = Factura(cliente, Tarjeta("4111222233334444", "Pedro Navas", 500000))
    factura.agregar_producto(inventario.buscar_producto("P-01"), 4)
    factura.agregar_producto(inventario.buscar_producto("P-03"), 2)
    factura.cerrar_venta()
    factura.imprimir_resumen()

    print()
    print(inventario.generar_reporte())
    bajos = [p.nombre for p in inventario.productos_bajo_stock(umbral=5)]
    print("Productos con stock bajo:", bajos)


if __name__ == "__main__":
    main()

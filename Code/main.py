import random

from producto import Producto
from cliente import Cliente
from medio_pago import Efectivo, Tarjeta, PagoRechazadoError
from inventario import Inventario
from factura import Factura

CATALOGO = [
    ("Arroz 1kg", 4500), ("Aceite 1L", 12000), ("Café 500g", 18000),
    ("Leche 1L", 4200), ("Huevos x30", 16500), ("Pan tajado", 6800),
    ("Azúcar 1kg", 4800), ("Chocolate 500g", 11500), ("Atún lata", 5900),
    ("Detergente 1kg", 14500),
]
NOMBRES = ["Elena", "Pedro", "Sara", "Mateo", "Diana", "Jorge", "Camilo", "Ana"]
APELLIDOS = ["Rojas", "Navas", "Gomez", "Silva", "Torres", "Rico", "Cruz", "Lopez"]


def crear_inventario():
    inventario = Inventario()

    productos = random.sample(CATALOGO, random.randint(5, len(CATALOGO)))
    for numero, (nombre, precio) in enumerate(productos, start=1):
        stock = random.randint(2, 40)
        inventario.registrar_producto(Producto(f"P-{numero:02d}", nombre, precio, stock))

    for documento in random.sample(range(1000000000, 1100000000), 5):
        nombre = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}"
        tipo = random.choice(["regular", "vip"])
        inventario.registrar_cliente(Cliente(str(documento), nombre, tipo))

    return inventario

def elegir_medio_pago(cliente):
    if random.choice([True, False]):
        return Efectivo(random.choice([50000, 100000, 200000]))
    numero = "".join(random.choice("0123456789") for _ in range(16))
    return Tarjeta(numero, cliente.nombre, random.choice([60000, 150000, 400000]))

def main():
    inventario = crear_inventario()
    print("INVENTARIO INICIAL")
    print(inventario.generar_reporte())

    cliente = random.choice(inventario.listar_clientes())
    factura = Factura(cliente, elegir_medio_pago(cliente))

    productos = inventario.listar_productos()
    elegidos = random.sample(productos, random.randint(1, min(4, len(productos))))
    for producto in elegidos:
        cantidad = random.randint(1, 5)
        try:
            factura.agregar_producto(producto, cantidad)
        except ValueError as error:
            print(f"Producto omitido: {error}")

    print("\nVENTA")
    try:
        factura.cerrar_venta()
        factura.imprimir_resumen()
    except PagoRechazadoError as error:
        print(f"Venta rechazada ({cliente.nombre}): {error}")
        print(f"Total que no se pudo cobrar: ${factura.calcular_total():,.0f}")
    except ValueError as error:
        print(f"No se pudo cerrar la venta: {error}")

    print("\nINVENTARIO FINAL")
    print(inventario.generar_reporte())
    bajos = [p.nombre for p in inventario.productos_bajo_stock(umbral=5)]
    print("Productos con stock bajo:", bajos)

if __name__ == "__main__":
    main()

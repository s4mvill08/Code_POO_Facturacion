# Code_POO_Facturación

Repositorio de código de facturación/Tienda

## Información detallada

El presente proyecto busca dar solución a una problemática que sucede en muchos entornos de los negocios que se manejan hoy en día: procesos manuales que no permiten una buena facturación de sus tiendas, lo que lleva a los siguientes inconvenientes:

- Errores en el cálculo de totales
- Falta de control sobre el inventario
- Dificultad para llevar un registro ordenado de las ventas
- Falta de flexibilidad en los medios de pago
- Ausencia de un sistema que diferencie automáticamente a los clientes

Ante esta problemática, se plantea el desarrollo de un sistema de facturación que permita gestionar productos, clientes, ventas y pagos de manera organizada, aplicando los principios de la Programación Orientada a Objetos.

El sistema debe permitir:

1. Registrar productos con su respectivo precio y cantidad disponible en inventario.
2. Registrar clientes y diferenciarlos según su tipo para aplicar descuentos automáticamente.
3. Administrar productos y clientes desde un módulo de inventario centralizado, que permite registrarlos, buscarlos, listarlos y consultar reportes.
4. Agregar productos a una factura, validando que haya stock suficiente antes de completar la venta.
5. Permitir el pago mediante diferentes métodos, sin que el resto del sistema deba conocer los detalles internos de cada tipo de pago.
6. Calcular automáticamente el total a pagar, incluyendo los descuentos correspondientes.
7. Generar un comprobante o factura final legible para el cliente.

## Estructura del proyecto

```
facturacion/
├── producto.py
├── cliente.py
├── medio_pago.py
├── inventario.py
├── factura.py
└── main.py
```

## producto.py

Contiene la clase `Producto`, que representa cada artículo que se vende en el negocio. Tiene atributos privados: código, nombre, precio y cantidad en stock, con validaciones como que el precio no pueda ser negativo. También tiene un método para verificar si hay stock disponible (`hay_stock`), otro para reducir el stock cuando se realiza una venta (`reducir_stock`) y otro para reponerlo (`aumentar_stock`).

Define las excepciones `PrecioInvalidoError`, `CantidadInvalidaError` y `StockInsuficienteError`.

## cliente.py

Contiene la clase `Cliente`, que representa a la persona que realiza la compra. Tiene atributos privados: documento, nombre y tipo de cliente (regular o VIP). Incluye un método (`calcular_descuento`) que devuelve el descuento correspondiente según el tipo de cliente: 0 % para regular y 10 % para VIP.

## medio_pago.py

Es el archivo donde se aplican principalmente la abstracción y el polimorfismo. La clase abstracta `MedioPago` define el contrato común (`procesar_pago` y `generar_comprobante`) y de ella se crean las distintas formas de pago:

- `Efectivo`: valida que el dinero entregado cubra el total y calcula el cambio.
- `Tarjeta`: valida que el cupo alcance y muestra solo los últimos cuatro dígitos en el comprobante.

Cada una procesa el pago y genera su comprobante a su manera, pero todas se usan igual desde el resto del programa. Si el pago no puede cubrirse, se lanza `PagoRechazadoError`.

## inventario.py

Contiene la clase `Inventario`, el módulo central que administra los productos y los clientes del negocio. Mantiene ambos registros de forma privada y ofrece:

- **Productos:** registrar, buscar por código, reabastecer, listar, consultar los de stock bajo y calcular el valor total del inventario.
- **Clientes:** registrar, buscar por documento, listar y filtrar por tipo (regular o VIP).
- **Reporte:** `generar_reporte` entrega un resumen del inventario y de los clientes registrados.

Si se intenta registrar un producto o cliente que ya existe, se lanza `RegistroDuplicadoError`.

## factura.py

Contiene la clase `Factura`, encargada de unir toda la información de una venta: el cliente que compra, los productos seleccionados, el medio de pago elegido y el cálculo del total con descuento incluido. Tiene un método para agregar productos (validando el stock disponible), otro para cerrar la venta y otro para imprimir el resumen final de la compra.

Al cerrar la venta, primero se procesa el pago y solo si es aprobado se descuenta el stock; si el pago falla, el inventario no se modifica.

## main.py

Es el archivo principal del programa, desde donde se ejecuta todo. Aquí se registran en el inventario los productos disponibles y los clientes, se busca al cliente que compra, se elige un medio de pago y se genera la factura final, mostrando en pantalla el resultado y el reporte de inventario actualizado. Este archivo no contiene lógica de negocio propia, solo se encarga de conectar y poner en marcha las demás clases.

## Conceptos de POO aplicados

- **Encapsulamiento:** atributos privados en `Producto`, `Cliente`, `Tarjeta`, `Efectivo`, `Factura` e `Inventario`; el stock solo cambia mediante métodos validados.
- **Abstracción:** `MedioPago` define qué debe hacer un medio de pago sin decir cómo.
- **Polimorfismo:** `Factura` usa cualquier medio de pago con las mismas llamadas, sin conocer su tipo.
- **Herencia:** `Efectivo` y `Tarjeta` heredan de `MedioPago`.
- **Composición:** `Factura` se compone de un cliente, un medio de pago y una lista de productos; `Inventario` agrupa productos y clientes.
- **Excepciones personalizadas:** errores propios del negocio para precio, cantidad, stock, pago y registros duplicados.

## Interfaz

El programa se ejecuta actualmente por consola mediante `main.py`.

# Code_POO_Facturación
Repositorio de código de facturación/Tienda

# Información detallada
El presente proyecto busca dar solución a una problemática que sucede en muchos entornos de los negocios que se manejan hoy en día, procesos manuales que no permiten una buena facturación de sus tiendas, manejando la facturación manual, que lleva a los siguientes inconvenientes:
•	Errores en el cálculo de totales
•	Falta de control sobre el inventario
•	Dificultad para llevar un registro ordenado de las ventas
•	Falta de flexibilidad en los medios de pago
•	Ausencia de un sistema que diferencie automáticamente a los clientes.
Ante esta problemática, se plantea el desarrollo de un sistema de facturación que permita gestionar productos, clientes, ventas y pagos de manera organizada, aplicando los principios de la Programación Orientada a Objetos. El sistema debe permitir:
1.	Registrar productos con su respectivo precio y cantidad disponible en inventario.
2.	Registrar clientes y diferenciarlos según su tipo para aplicar descuentos automáticamente.
3.	Agregar productos a una factura, validando que haya stock suficiente antes de completar la venta.
4.	Permitir el pago mediante diferentes métodos, sin que el resto del sistema deba conocer los detalles internos de cada tipo de pago.
5.	Calcular automáticamente el total a pagar, incluyendo los descuentos correspondientes.
6.	Generar un comprobante o factura final legible para el cliente.
Archivo: producto

Contendrá la clase Producto, que representa cada artículo que se vende en el negocio. Tendrá atributos privados como código, nombre, precio y cantidad en stock. Con validaciones como que el precio no pueda ser negativo. También tendrá un método para verificar si hay stock disponible y otro para reducir el stock cuando se realice una venta.

Archivo: cliente

Contendrá la clase cliente, que representa a la persona que realiza la compra. Tendrá atributos privados como nombre y tipo de cliente (regular o VIP). Y un método que calcule el descuento correspondiente según el tipo de cliente.

Archivo: medio_pago

Este archivo es donde se aplicarán principalmente la abstracción y el polimorfismo. A partir de ella se crearán distintas formas de pago (por ejemplo, efectivo y tarjeta), cada una con su propia manera de procesar el pago y de generar su comprobante, aunque todas se usen de la misma forma desde el resto del programa.

Archivo: factura

Contendrá la clase Factura, encargada de unir toda la información de una venta: el cliente que compra, los productos seleccionados, el medio de pago elegido y el cálculo del total con descuento incluido. También tendrá un método para agregar productos a la factura y otro para imprimir el resumen final de la compra.

Archivo: main

Este será el archivo principal del programa, desde donde se ejecuta todo. Aquí se crearán los productos disponibles, se registrará un cliente, se elegirá un medio de pago y se generará la factura final, mostrando en pantalla el resultado. Este archivo no contendrá lógica de negocio propia, solo se encargará de conectar y poner en marcha las demás clases.


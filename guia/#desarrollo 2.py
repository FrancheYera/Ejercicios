#desarrollo 2
ingresos = int (input("ingrese los salario del usuario : "))
casa = int (input("ingrese el precio de la casa : "))


if 80000 <= ingresos:
    descuento1 = ingresos * 0.15
    print ("usted cuenta con un descuento de:", descuento1)
    pago_mensual = (casa - descuento1) / (10 * 12)
    print ("el resto se distribuirá en pagos mensuales a pagar en 10 años, el cual serian: ", pago_mensual)
else:
    descuento2 = ingresos * 0.30
    print ("usted cuenta con un descuento de:", descuento2)
    pago_mensual = (casa - descuento2) / (7 * 12)
    print ("el resto se distribuirá en pagos mensuales a pagar en 7 años, el cual serian: ", pago_mensual)

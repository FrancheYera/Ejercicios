#DESARROLLO 2 WHILE

while True:
    ingresos = int(input("Ingrese los ingresos del usuario: "))
    casa = int(input("Ingrese el precio de la casa: "))

    if ingresos >= 80000:
        descuento1 = ingresos * 0.15
        print("Usted cuenta con un descuento de:", descuento1)
        pago_mensual = (casa - descuento1) / (10 * 12)
        print("El resto se distribuirá en pagos mensuales a pagar en 10 años, los cuales serían: ", pago_mensual)
    else:
        descuento2 = ingresos * 0.30
        print("Usted cuenta con un descuento de:", descuento2)
        pago_mensual = (casa - descuento2) / (7 * 12)
        print("El resto se distribuirá en pagos mensuales a pagar en 7 años, los cuales serían: ", pago_mensual)

    continuar = input("¿Desea realizar otro cálculo? (si/no): ")
    if continuar.lower() != 'si':
        break

#DESARROLLO 1 WHILE   

clientes = []

precio_asiento = int(input("Ingrese el precio de la entrada: $"))

descuento_categoria1 = 0
descuento_categoria2 = 0
descuento_categoria3 = 0
descuento_categoria4 = 0
descuento_categoria5 = 0

while True:
    edad = int(input("Ingrese la edad del cliente (o 0 para terminar): "))
    if edad == 0:
        break

    if 5 <= edad <= 14:
        descuento = precio_asiento * 0.35
        descuento_categoria1 += descuento

    elif 15 <= edad <= 19:
        descuento = precio_asiento * 0.25
        descuento_categoria2 += descuento

    elif 20 <= edad <= 45:
        descuento = precio_asiento * 0.1
        descuento_categoria3 += descuento

    elif 46 <= edad <= 65:
        descuento = precio_asiento * 0.25
        descuento_categoria4 += descuento

    elif 66 <= edad:
        descuento = precio_asiento * 0.35
        descuento_categoria5 += descuento

    else:
        print("La edad ingresada no es válida.")
        continue

    clientes.append({"edad": edad, "descuento": descuento})

print("\nDescuentos por cliente:")
for cliente in clientes:
    print(f"Edad: {cliente['edad']}, Descuento: ${cliente['descuento']}")

print("\nTotal de descuentos perdidos por categoría:")
print("Categoría 1 (5 - 14 años): $", descuento_categoria1)
print("Categoría 2 (15 - 19 años): $", descuento_categoria2)
print("Categoría 3 (20 - 45 años): $", descuento_categoria3)
print("Categoría 4 (46 - 65 años): $", descuento_categoria4)
print("Categoría 5 (66 años en adelante): $", descuento_categoria5)

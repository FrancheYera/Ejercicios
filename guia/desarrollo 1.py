

#DESARROLLO 1
edad_cliente = int(input("Ingrese la edad del cliente: "))
precio_asiento = int(input("Ingrese el precio de la entrada: "))

if 5<= edad_cliente <= 14:
    categoria =  precio_asiento * 0.35
    
elif 15<= edad_cliente <= 19:
     categoria =  precio_asiento * 0.25
     
elif 20<= edad_cliente <= 45:
     categoria =  precio_asiento * 0.1
     
elif 46<= edad_cliente <= 65:
     categoria =  precio_asiento * 0.25
     
elif 66<= edad_cliente:
     categoria =  precio_asiento * 0.35

print ("el dinero perdido luego de realizar el descuento son:", categoria)





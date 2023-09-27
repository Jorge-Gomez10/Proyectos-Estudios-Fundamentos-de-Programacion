def calcular_descuento (monto_total, porcentaje_descuento):
    #Calcula el descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    #Calcula el valor total a pagar
    total_a_pagar = monto_total - descuento
    return  descuento, total_a_pagar

#Solicita al usuario que ingrese el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

#Llama a la funcion calcular_descuento
descuento, total_a_pagar = calcular_descuento(monto_total, 10)

#Muestra el descuento y el valor total a pagar
print(f"Descuento aplicado: $ {descuento:.2f}")
print(f"Total a pagar: ${total_a_pagar: .2f}")

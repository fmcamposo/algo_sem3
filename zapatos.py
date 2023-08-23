print("Venta de Zapatos")
valor_zapato=20000
print(f"El valor de cada par de zapatos sin importar el numero es de ${valor_zapato}")
cant=int(input("Indique la cantidad de pares de zapatos que desea:"))
total=valor_zapato*cant
if total>=40000:
    print("el envio es gratis")
else:
    print("tendra un recargo por envio de $3000 pesos extra")
    total=total+3000
print(f"El total a pagar es de :{total}")


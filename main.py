total=0
print("Cine Duoc")
print("#########")
print("1) Pertenece a Duoc")
print("2) No pertenece a Duoc")
op=int(input("Seleccione (1-2):"))
pertenece=False
if op==1 or op==2:
    if op==1:
        pertenece=True
    print("Seleccione el tipo de entrada")
    print("1) Estreno")
    print("2) Normal")
    op_te=int(input("Seleccione (1-2):"))
    if op_te==1 or op_te==2:
        valor=0
        if op_te==1:
            valor=4800
        else:
            valor=2900
        print(f"el valor de la entrada es de: ${valor}")
        cantidad=int(input("indique cantidad de entradas a comprar:"))
        total=(valor*cantidad)
        print(f"en entradas se debe pagar ${total}")
        if pertenece:
            print("por pertenecer a Duoc tendra un descuento de 30%")
            descuento=int(total*0.3)
            print(f"El descuento es de ${descuento}")
            total=total-(descuento)
            print(f"El total a pagar en entradas con el descuento es de ${total}")
        resp=input("Desea agregar Palomitas (s/n):")
        if resp.upper()=='S':
            print("1) Palomitas pequeñas")
            print("2) Palomitas medianas")
            print("3) Palomitas grande")
            op_palo=int(input("Seleccione (1-3):"))
            valor_palo=0
            if op_palo>=1 and op_palo<=3:
                if op_palo==1:
                    valor_palo=2500
                if op_palo==2:
                    valor_palo=4500
                if op_palo==3:
                    valor_palo=7800
                cantidad_palo=int(input("Indique la cantidad:"))
                print(f"Valor Palomitas: ${valor_palo} / Cantidad: {cantidad_palo}")
                print(f"Total en Palomitas:${cantidad_palo*valor_palo}")
                total=total+(cantidad_palo*valor_palo)
        resp=input("Desea agregar Bebidas (s/n):")
        if resp.upper()=='S':
            print("1) Bebida pequeñas")
            print("2) Bebida medianas")
            print("3) Bebida grande")
            op_beb=int(input("Seleccione (1-3):"))
            valor_beb=0
            if op_beb>=1 and op_beb<=3:
                if op_beb==1:
                    valor_beb=1000
                if op_beb==2:
                    valor_beb=1250
                if op_beb==3:
                    valor_beb=2000
                total=total+valor_beb
        print(f"Total a Pagar es de ${total}")
        monto=int(input("ingrese el monto a pagar:"))
        if monto>=total:
            if monto>total:
                vuelto=int(monto-total)
                print(f"Su vuelto es de ${vuelto}")
            else:
                print("Pago justo")
            print("Gracias por su compra")            
        else:
            print("monto insufience, no se puede efectuar la venta")
    else:
        print("opcion de tipo de entrada incorrecto")
else:
    print("selecciono una opcion no valida")

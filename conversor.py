print("Convertidor a Pesos Chilenos")
print("1) Dolar australiano a Pesos Chilenos")
print("2) Peso argentino a Pesos Chilenos")
print("3) Yen a Pesos Chilenos")
op=int(input("Seleccione (1-3):"))
op_text=""
valor=0
if op>=1 and op<=3:
    if op==1:
        op_text="Dolar Australiano"
        valor=563.09
    if op==2:
        op_text="Peso Argentino"
        valor=2.48
    if op==3:
        op_text="Yen"
        valor=6
    print(f"de {op_text} a Peso - Valor de {op_text} es de ${valor} pesos chilenos")    
    cantidad=int(input("Cantidad:"))
    print(f"{cantidad} {op_text} son Total :{cantidad*valor} pesos chilenos")
else:
    print("opcion de convertidor incorrecta")
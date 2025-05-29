# ingresar una cifra x y vamos a calcular
# billetes de 50,20,10 y 5 tenemos que devolver al usuario

cantidad = int(input("ingrese la cantidad de $ a retirar: "))

can_50 = 0
can_20 = 0
can_10 = 0
can_5 = 0
total = cantidad

 # que la cantidad ya es valida!!
  
while total < 0:

    if total >= 50_000:
        # can_50 += 1
        can_50 = can_50 + 1
        # total -= 50_000
        total = total - 50_000
    elif total >= 20_000:
        can_20 += 1
        total -= 20_000
    elif total >= 10_000:
        can_10 += 1
        total -= 10_000   
    elif total >= 5_000:
        can_5 += 1
        total -= 5_000
    else: 
        print ("no tenemos fondos suficientes :c ")
        break

print(f"cantidad de dinero: {cantidad}/n50k: {can_50}/n20k {can_20}/n10k {can_50}/n5k {can_50}")     


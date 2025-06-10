import random
numero = random.sample
numero_persona = random.sample

print("bienvenido a la loteria epica")
print("introduce tu nombre",) 
usuario = input()
print("bienvenido", usuario, "a la loteria epica")
boletos = []
numero_de_boleto = []
contador_iguales = []
i = []
def mostrar_menu():
    print("menu")
    print("1.comprar boletos")
    print("2.generacion de numeros ganadores")
    print("3.comparacion de resultados")
    print("4.premio")
    print("4.salir")
while True:
    mostrar_menu()
    opcion = input ("introduce una opcion a realizar\n ")

    if opcion == "1":
        print("desea generar los numeros automaticamente?\n")
        print("SI / NO")
        respuesta = input().strip().upper()
        if respuesta == "SI":
            numero_de_boleto = random.sample(range(1,49),6)
            print("los numeros de tu boleto son\n", numero_de_boleto)   
        else:
            numero_de_boleto = input("introduce los numeros de tu boleto separados por comas:\n")
            numero_de_boleto = [int(x) for x in numero_de_boleto.split(",")]
            if len(numero_de_boleto) != 6:
                print("debes introducir exactamente 6 numeros")
                continue
            if any(x < 1 or x > 49 for x in numero_de_boleto):
                print("los numeros deben estar entre 1 y 49")
                continue
            print("los numeros de tu boleto son\n", numero_de_boleto)
    elif opcion == "2":
        print ("los numeros ganadores son\n", numero)
        numero = random.sample(range(1,49),6)
        print (numero)
    elif opcion == "3":
        print (numero_de_boleto)
        print (numero)
        

















             

             
         

    #    try:
     #       numero = (numero_de_boleto)
      #      if numero > 49:
       #         print("boleto comprado")
        #    else:
         #        print("numero no valido")    
#
 #       except ValueError:
  #              print("eso no es un numero valido")
   #             if 1 <= numero <= 49:
    #                print("bien")
     #           else:
      #              print("el numero no esta en el rango peermitido")
     
        


        


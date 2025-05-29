productos = ["pan","leche","cafe","tostado","coca-cola"]
#           0       1   2       3   4
precios = [1500, 3700, 8500, 1000, 4500]




menu = """
  _,-""`""-~`)
(`~_,=========l
 |---,___.-.__,l
 |        o     \ ___  _,,,,_     _.--.
  \      `^`    /`_.-"~      `~-;`     l
   \_      _  .'                 `,     |
     |`-                           \'__/ 
    /                      ,_       \  `'-. 
   /    .-""~~--.            `"-,   ;_    /
  |              \               \  | `""`
   \__.--'`"-.   /_               |'
              `"`  `~~~---..,     |
 jgs                         \ _.-'`-.
                              \       l
                               '.     /
                                 `"~"`
MENU
    1.productos
    2.carrito
    3.finalizar
"""

while True:
    print(menu)
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        print("gracias por comprar")
        break
    else:
        print("opcion no valida")
    





nombretienda = "mi tienda"
print(f"bienvenidos a {nombretienda}")
print(f"productos disponibles : {len(productos)}")

for posicion in range(5):
    print("--------------------")
    print(f"{posicion + 1}. {productos[posicion]} $ {precios[posicion]}")
    print("--------------------")

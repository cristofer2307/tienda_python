
nuevo_tablero = []
listas = []
targeta = []
datos = []
nueva_lista = []
tarjeta_nueva = []


def menu_gestor_de_tareas ():
    print("1.Gestión de tablero")
    print("2.Gestión de listas")
    print("3.Gestión de tarjetas")
    print("4.Persistencia de datos")

def menu_gestor_de_tableros ():
    print("1.crear un nuevo tablero")
    print("2.ver todos los tableros")
    print("3.actualizar el nombre de un tablero")
    print("4.eliminar una tablero")

def menu_gestor_de_listas ():
    print("1.crear una lista dentro de un tablero")
    print("2.ver todas las listas de un tablero")
    print("3.actualizar el nombre de una lista")
    print("4.eliminar una lista")

def menu_gestor_de_tarjetas ():
    print("1.crear una tarjeta de tarea dentro de una lista")
    print("2.ver todas las tarjetas dentro de una lista")
    print("3.actualizar una tarjeta(titulo, descripcion, estado)")
    print("4.eliminar una tarjeta")

def menu_historial_de_datos ():
    print("cosas guardadas")

print("----------------------------")
print("Gestor de Tareas CampusTask")
print("----------------------------")
print("ingrese su nombre:")
usuario = input()
print("----------------------------")
print("tareas de:", usuario)
print("----------------------------")
while True:
    menu_gestor_de_tareas()
    print("----------------------------")
    opcion = input("ingrese una opcion a realizar: ")
    print("----------------------------")
    if opcion == "1" :
        print(menu_gestor_de_tableros())
        print("----------------------------")
        opcion2 = input("ingresa una opcion a realizar: ")
        print("----------------------------")
        if opcion2 == "1":
            input("ingresa el nombre de tu nuevo tablero: ")
            nuevo_tablero = input
            print("----------------------------")
        elif opcion2 == "2":
            print(nuevo_tablero)
        elif opcion2 == "3":
            input("ingresa el nombre del tablero al que desea cambiarle el nombre: ")
        elif opcion2 == "4":
            input("ingresa el nombre del tablero que desea eliminar: ")
        else:
            print("debe seleccionar una opcion valida")
    elif opcion == "2":
        print(menu_gestor_de_listas())
        opcion3 = input("ingresa una opcion a realizar:")
        print("----------------------------")
        if opcion3 =="1":
            nueva_lista = input("ingresa el nombre del tablero en el que desea crear una lista")
        elif opcion3 == "2":
            print(nueva_lista)
        elif opcion3 == "3":
            print("inrese el nombre de la lista a la que desea cambiarle el nombre")
        elif opcion3 == "4":
            print("ingrese el nombre de la lista que desea eliminar")
        else:
            print("debe seleccionar una opcion valida")
    elif opcion == "3":
        print(menu_gestor_de_tarjetas())
        opcion4 = input("ingresa una opcion a realizar:")
        print("----------------------------")
        if opcion4 == "1":
            tarjeta_nueva = input("ingresa el nombre de la lista a la que le desea crear una tarjeta de tarea")
        elif opcion4 == "2":
            print(tarjeta_nueva)
        elif opcion4 == "3":
            print("inrese el nombre de la tarjeta a la que desea cambiarle el nombre")
        elif opcion4 == "4":
            print("ingrese el nombre de la tarjeta que desea eliminar")
        else:
            print("debe seleccionar una opcion valida")
    elif opcion == "4":
        print(menu_historial_de_datos())
    else:
        print("debe seleccionar una opcion valida")
        

            



import json
import os

FILENAME = 'contacts.json'

def cargar_contactos():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def guardar_contactos(contactos):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(contactos, file, indent=4, ensure_ascii=False)


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_no_vacio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print(" Este campo no puede estar vacio.")


def crear_contacto(contactos):
    limpiar_consola()
    print(" Crear contacto")
    nombre = input_no_vacio("Nombre: ")
    telefono = input_no_vacio("Telefono: ")
    email = input_no_vacio("Email: ")

    nuevo_id = max([c["ID"] for c in contactos], default=0) + 1
    nuevo_contacto = {
        "ID": nuevo_id,
        "Nombre": nombre,
        "Telefono": telefono,
        "Email": email}

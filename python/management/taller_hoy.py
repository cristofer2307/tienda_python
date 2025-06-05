#abrir el archivo en modo lectura
try:
    with open('notas.txt', 'r', encoding='utf-8') as archivo:
        for numero , linea in enumerate(archivo, start=1):
            print(f"{numero}: {linea.strip()}")
except FileNotFoundError:
    print("CREA EL FOKIN ARCHIVO.")
with open("diario.txt", "a") as archivo:
    archivo.write("estudié\n")
    archivo.write("dormí\n")  
    with open("diario.txt", "r") as archivo:
        contenido = archivo.read()
        print(" Contenido del archivo:")
        print(contenido)



usuarios = [
    {"id": 1, "nombre": "cristofer", "ciudad": "Bogotá"},
    {"id": 2, "nombre": "Cris", "ciudad": "Medellín"},
    {"id": 3, "nombre": "cristian", "ciudad": "Bogotá"},
    {"id": 4, "nombre": "cristiano", "ciudad": "Barranquilla"},
    {"id": 5, "nombre": "cristobal", "ciudad": "Cartagena"}]

#crear archivo CSV
with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["id", "nombre", "ciudad"]
    import csv  
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()        
    escritor.writerows(usuarios)  

print("Archivo usuarios.csv creado exitosamente.")


#leer el archivo CSV 
try:
        with open("usuarios.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
        print("\nUsuarios que viven en Bogotá:")
        for fila in lector:
            if fila["ciudad"] == "Bogotá":
                print(f"ID: {fila['id']}, Nombre: {fila['nombre']}")
except FileNotFoundError:
    print("Error: El archivo usuarios.csv no se encontró.")       
import json


def manejar_productos_json():
    productos = {
        "productos": [
            {"id": 1, "nombre": "moniutor", "precio": 250},
            {"id": 2, "nombre": "Mouse", "precio": 25},
            {"id": 3, "nombre": "Teclado", "precio": 75}]}

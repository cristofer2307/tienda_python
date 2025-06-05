def leerArchivo(path:str) -> list:
    with open(path, mode= "r") as file:
        return(file.readlines())
    
def escribirArchivo(path: str, lineas: list, mode = "a"):
    with open(path,mode=mode) as file:
        file.writelines(lineas)
        
nuevasLineas = ["skill", "python \n", "grupo", "A2"]

escribirArchivo("archivo.txt", nuevasLineas)
datos = leerArchivo("archivo.txt")
print(datos)

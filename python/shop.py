score = (["bajo", 25], ["aceptable", 50], ["sobresaliente",75] ["excelente", 90])

def funcion(nota):
    for i, n in enumerate(score, start=1 ):
        if(nota >= n[1] and nota <= n[2]):
            print(f"la nota es: {i} - {n[0]}")
            break

def promedios():
    mensaje = "notas: \n"
    for i, n in enumerate(score, start= 1):
        mensaje += f"{i}. {n[1]} a {n[2]} -> {n[0]} \n"
    return mensaje


nota = float(input("ingrese la nota: ")) 
print(promedios())
funcion(nota)  


print(score)
print(score[0])
print(score[0][0])
print(score[0][1])
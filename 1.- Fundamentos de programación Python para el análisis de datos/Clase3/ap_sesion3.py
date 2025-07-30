respuesta = input("¿Deseas ingresar un nuevo estudiante? (s/n): ")
estudiantes = []

while respuesta == "s":

    nombre = input("Introduce el nombre del estudiante: ")
    calificacion_matematica = int(input("Introduce la calificación de Matemáticas: "))
    calificacion_ciencias = int(input("Introduce la calificación de Ciencias: "))
    calificacion_ingles = int(input("Introduce la calificación de Inglés: "))
    
    promedio = (calificacion_matematica + calificacion_ciencias + calificacion_ingles) / 3

    if promedio >= 90:
        mensaje = "Excelente"
    elif 75 <= promedio < 90:
        mensaje = "Bien"
    elif 60 <= promedio < 75:
        mensaje = "Necesita mejorar"
    else:
        mensaje = "Reprobado"
    print(f"{mensaje}. La calificación de {nombre} es {promedio}.")
    
    estudiantes.append({"Estudiante": nombre, "Comentario": mensaje})
    respuesta = input("¿Deseas ingresar otro estudiante? (s/n): ")

for item in estudiantes:
    print(item["Estudiante"], item["Comentario"])

for item in estudiantes:
    item["Comentario"] = "¡Puntuación perfecta!" if promedio == 100 else ""
    print(item["Estudiante"], item["Comentario"])

print("Programa finalizado.")
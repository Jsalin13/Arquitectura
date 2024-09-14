def mostrar_usuario(usuario):
    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")

def solicitar_datos_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    return {'nombre': nombre, 'edad': edad}
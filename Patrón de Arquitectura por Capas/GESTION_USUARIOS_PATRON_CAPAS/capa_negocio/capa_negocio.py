from capa_datos.capa_datos import guardar_usuario

def validar_usuario(usuario):
    if not usuario['nombre'] or usuario['edad'] <= 0:
        raise ValueError("Datos del usuario no válidos")
    return True

def agregar_usuario(usuario):
    if validar_usuario(usuario):
        guardar_usuario(usuario)
        return "Usuario agregado con éxito"
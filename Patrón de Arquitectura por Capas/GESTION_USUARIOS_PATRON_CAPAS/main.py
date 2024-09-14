
from capa_presentancion.capa_presentacion import solicitar_datos_usuario, mostrar_usuario
from capa_negocio.capa_negocio import agregar_usuario
from capa_datos.capa_datos import usuarios

def main():
    usuario = solicitar_datos_usuario()
    mensaje = agregar_usuario(usuario)
    print(mensaje)
    print("\nLista de usuarios:")
    for u in usuarios:
        mostrar_usuario(u)

if __name__ == "__main__":
    main()
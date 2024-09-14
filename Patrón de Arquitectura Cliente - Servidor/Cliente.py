import socket

def start_client(host='localhost', port=65432):
    # Crear un socket para el cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Conectar al servidor
        client_socket.connect((host, port))

        while True:
            # Leer mensaje del usuario
            message = input("Escribe un mensaje para enviar al servidor (o 'salir' para terminar): ")
            if message.lower() == 'salir':
                print("Cerrando conexión.")
                break
            # Enviar el mensaje al servidor
            client_socket.sendall(message.encode())
            # Recibir la respuesta del servidor
            response = client_socket.recv(1024)
            print(f"Respuesta del servidor: {response.decode()}")

if __name__ == "__main__":
    start_client()

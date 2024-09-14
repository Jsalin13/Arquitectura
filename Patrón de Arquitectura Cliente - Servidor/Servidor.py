import socket
import threading

def handle_client(client_socket):
    with client_socket:
        while True:
            try:
                # Recibir datos del cliente
                message = client_socket.recv(1024)
                if not message:
                    break
                # Convertir el mensaje a mayúsculas
                message_upper = message.decode().upper()
                print(f"Mensaje recibido del cliente: {message.decode()}")
                print(f"Mensaje transformado a mayúsculas: {message_upper}")
                # Enviar el mensaje transformado al cliente
                client_socket.sendall(message_upper.encode())
            except ConnectionResetError:
                print("Conexión con el cliente perdida.")
                break

def start_server(host='localhost', port=65432):
    # Crear un socket para el servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Enlazar el socket a la dirección y puerto especificados
        server_socket.bind((host, port))
        # Escuchar conexiones entrantes
        server_socket.listen()
        print(f"Servidor escuchando en {host}:{port}")

        while True:
            # Aceptar una conexión entrante
            client_socket, addr = server_socket.accept()
            print(f"Conectado a {addr}")
            # Manejar la conexión en un hilo separado
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    start_server()

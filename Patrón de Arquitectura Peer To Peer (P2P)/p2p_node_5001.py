import socket
import threading

class P2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor P2P iniciado en {self.host}:{self.port}")
        
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Conexión de {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Mensaje recibido: {message}")
                    self.broadcast(message, client_socket)
                else:
                    break
            except ConnectionResetError:
                break
        client_socket.close()

    def broadcast(self, message, client_socket):
        for peer in self.peers:
            if peer != client_socket:
                try:
                    peer.send(message.encode())
                except Exception as e:
                    print(f"Error enviando mensaje a un par: {e}")

    def connect_to_peer(self, peer_host, peer_port):
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((peer_host, peer_port))
            self.peers.append(peer_socket)
            print(f"Conectado a par {peer_host}:{peer_port}")
            threading.Thread(target=self.listen_to_peer, args=(peer_socket,), daemon=True).start()
        except Exception as e:
            print(f"No se pudo conectar a {peer_host}:{peer_port}: {e}")

    def listen_to_peer(self, peer_socket):
        while True:
            try:
                message = peer_socket.recv(1024).decode()
                if message:
                    print(f"Mensaje de un par: {message}")
                else:
                    break
            except Exception as e:
                print(f"Error al recibir mensaje de un par: {e}")
                break
        peer_socket.close()

if __name__ == "__main__":
    node = P2PNode('localhost', 5001)  # Cambiar el puerto a 5001
    node.start()
    node.connect_to_peer('localhost', 5000)  # Conectar al nodo en 5000

    while True:
        message = input("Escribe un mensaje para enviar: ")
        for peer in node.peers:
            peer.send(message.encode())

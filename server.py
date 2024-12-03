import socket
import threading

# Function to handle clients
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{client_address}] {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    print(f"[DISCONNECT] {client_address} disconnected.")
    client_socket.close()
    clients.remove(client_socket)

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

clients = []

print("[STARTING] Server is starting...")
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {len(clients)}")
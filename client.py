import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Start the thread to receive messages
thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

# Main loop to send messages
while True:
    message = input()
    if message.lower() == 'exit':
        client.close()
        break
    client.send(message.encode('utf-8'))
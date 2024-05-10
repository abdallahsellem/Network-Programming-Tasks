

import socket
import threading
import ast
import sys

def handle_client(client_socket, client_address):
    while True:
        try:
            data_size = int.from_bytes(client_socket.recv(8), byteorder='big')
            data = client_socket.recv(data_size).decode('utf-8')
            if not data:
                break
            print(f"Received from {client_address}: {data}")

            recipient_address, message = data.split(':', 1)

            recipient_socket = None
            for client in clients:
                if client[1] == ast.literal_eval(recipient_address): 
                    recipient_socket = client[0]
                    break
            if recipient_socket:
                message=message.encode('utf-8') 
                message_size = sys.getsizeof(message)
                recipient_socket.send(message_size.to_bytes(8,byteorder='big'))
                recipient_socket.send(message)
            else:
                print(f"Recipient not found: {recipient_address}")

        except socket.error:
            break

    print(f"Connection closed with {client_address}")
    clients.remove((client_socket, client_address))
    client_socket.close()

def start_server():
    host = 'localhost'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append((client_socket, client_address))
        print(f"Connected with {client_address}")
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == '__main__':
    clients = []
    start_server()
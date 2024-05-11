import socket
import threading
import sys
def receive_messages(sock):
    while True:
        try:
            data_size = int.from_bytes(sock.recv(8), byteorder='big')
            data = sock.recv(data_size).decode('utf-8')
            print(data)
        except socket.error:
            break

def send_message(sock):
    while True:
        message = input()
        recipient = input("Enter recipient address (host:port): ")
        data = f"{recipient}:{message}"
        message=data.encode('utf-8') 
        message_size = sys.getsizeof(message)
        sock.send(message_size.to_bytes(8,byteorder='big'))
        sock.send(message)

def start_chat():
    host = 'localhost'
    port = 8000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(sock,))
    send_thread.start()

if __name__ == '__main__':
    start_chat()

import socket
import sys
import secrets
import threading

IP = '0.0.0.0'
PORT = 2222

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    while True:
        listen(server)

def listen(server):
    client, address = server.accept()
    client_handel = threading.Thread(target=client_handler, args=(client,))
    client_handel.start()

def client_handler(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(request.decode("utf-8"))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('programa finalizado')
        sys.exit(130)
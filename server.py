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



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('programa finalizado')
        sys.exit(0)

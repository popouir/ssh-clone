import socket
from argparse import ArgumentParser, Namespace
import sys

parser = ArgumentParser()

parser.add_argument('target', help='the target ip, by default 127.0.0.1', default='127.0.0.1')

args: Namespace = parser.parse_args()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 2222
peticion_string = 'pssh_p'

def main():
    client.connect((args.target, PORT))
    client.send(peticion_string.encode("utf-8"))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

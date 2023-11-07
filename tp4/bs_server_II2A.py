import socket
from sys import exit
import argparse
import logging

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", action="store", type=int, default=13337, help='precise a port to bind the program, default is 13337')

args = parser.parse_args()

if args.port < 0 or args.port > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif args.port >= 0 and args.port <= 1024:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)

host = '10.1.1.11'
port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

logging.basicConfig(format=f'%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# logging.info(f'Le serveur tourne sur {host}:{port}')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

s.listen(1)

while True:
    
    conn, addr = s.accept()

    print(f"Un client vient de se co et son IP c'est {addr[0]}")

    conn.sendall(b'Hi mate!')

    try:
        data = conn.recv(1024).decode()
        
        if not data: continue

        print(f"{data}")
        
        if "meo" in data:
            conn.sendall(bytes('Meo à toi confrère.', 'utf-8'))
        elif "waf" in data:
            conn.sendall(b'ptdr t ki')
        else:
            conn.sendall(b'Mes respects humble humain.')

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
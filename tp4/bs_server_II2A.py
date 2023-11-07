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

logging.basicConfig(format=f'%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logging.info(f'Le serveur tourne sur {host}:{port}')

s.listen(1)

while True:
    
    conn, addr = s.accept()
    
    ip_client = addr[0]
    
    logging.info(f"Un client {ip_client} s'est connecté.")

    # print(f"Un client vient de se co et son IP c'est {ip_client}")

    try:
        data = conn.recv(1024).decode()
        
        if not data: continue
        
        logging.info(f"Le client {ip_client} a envoyé {data}.")

        # print(f"{data}")
        server_response = ""
        
        if "meo" in data:
            server_response = "Meo à toi confrère."
        elif "waf" in data:
            server_response = "ptdr t ki"
        else:
            server_response = "Mes respects humble humain."
            
        conn.sendall(bytes(server_response, 'utf-8'))
        
        logging.info(f"Réponse envoyée au client {ip_client} : {server_response}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
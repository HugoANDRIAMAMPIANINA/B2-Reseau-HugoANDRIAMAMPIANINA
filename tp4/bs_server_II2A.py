import socket
from sys import exit
import argparse
import logging
from threading import Timer

class CustomFormatter(logging.Formatter):
    # Pour des logs en couleur dans la console
    
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    # bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s %(levelname)s %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'

    FORMATS = {
        logging.DEBUG: grey + format + datefmt + reset,
        logging.INFO: grey + format + datefmt + reset,
        logging.WARNING: yellow + format + datefmt + reset,
        logging.ERROR: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def timeout():
    logger.warning(f'Aucun client depuis plus de une minute.')


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


logger = logging.getLogger("Program")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)

# logging.basicConfig(format=f'%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger.info(f'Le serveur tourne sur {host}:{port}')


s.listen(1)

last_client_timer = Timer(60,timeout)
last_client_timer.start()

while True:
    
    if last_client_timer.finished:
        print("lala")
        last_client_timer.cancel()
        last_client_timer = Timer(60,timeout)
        last_client_timer.start()
    
    conn, addr = s.accept()
    last_client_timer.cancel()
    
    ip_client = addr[0]
    
    logger.info(f"Un client {ip_client} s'est connecté.")

    # print(f"Un client vient de se co et son IP c'est {ip_client}")

    try:
        data = conn.recv(1024).decode()
        
        if not data: continue
        
        logger.info(f"Le client {ip_client} a envoyé {data}.")

        # print(f"{data}")
        server_response = ""
        
        if "meo" in data:
            server_response = "Meo à toi confrère."
        elif "waf" in data:
            server_response = "ptdr t ki"
        else:
            server_response = "Mes respects humble humain."
            
        conn.sendall(bytes(server_response, 'utf-8'))
        
        logger.info(f"Réponse envoyée au client {ip_client} : {server_response}")
        last_client_timer = Timer(60,timeout)
        last_client_timer.start()

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
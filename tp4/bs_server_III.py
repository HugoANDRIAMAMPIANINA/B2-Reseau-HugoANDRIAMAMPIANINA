import socket
from sys import exit
import logging
from color_formatter import ColoredFormatter


host = '10.1.1.11'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

logger = logging.getLogger("colored_logger")
logger.setLevel(logging.INFO)

color_formatter = ColoredFormatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log_file_path = '/var/log/bs_server/bs_server.log'
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(color_formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(color_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info(f'Le serveur tourne sur {host}:{port}')

s.listen(1)

while True:
    
    conn, addr = s.accept()
    
    ip_client = addr[0]
    
    logger.info(f"Un client {ip_client} s'est connecté.")

    try:
        calculation = conn.recv(1024).decode()
        
        if not calculation: continue
        
        logger.info(f"Calcul reçu du client {ip_client} : {calculation}.")

        result = eval(calculation)
            
        conn.sendall(bytes(str(result), 'utf-8'))
        
        logger.info(f"Résultat envoyée au client {ip_client} : {result}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
import socket
from sys import exit
import re
import logging
from color_formatter import ColoredFormatter


host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

color_formatter = ColoredFormatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
error_color_formatter = ColoredFormatter('%(levelname)s %(message)s')

log_file_path = '/var/log/bs_client/bs_client.log'
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(color_formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(error_color_formatter)
console_handler.setLevel(logging.ERROR)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

try:
    s.connect((host, port))
    logger.info(f"Connexion réussie à {host}:{port}.")
except:
    logger.error(f"Impossible de se connecter au serveur {host} sur le port {port}.")
    exit(1)

message = input("Que veux-tu envoyer au serveur : ")

if type(message) is not str:
    raise TypeError("Ici on veut que des strings !")
    
is_meo_or_waf_pattern = re.compile('.*?((meo)|(waf))')

if not is_meo_or_waf_pattern.match(message):
    raise TypeError("L'entrée doit contenir soit 'meo' soit 'waf'")
    
s.sendall(bytes(message, 'utf-8'))

logger.info(f"Message envoyé au serveur {host} : {message}.")

server_response = s.recv(1024).decode()

logger.info(f"Réponse reçue du serveur {host} : {server_response}.")

s.close()

exit(0)
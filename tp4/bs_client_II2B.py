import socket
from sys import exit
import re
import logging
from color_formatter import ColoredFormatter

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.ERROR)

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

info_color_formatter = ColoredFormatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
error_color_formatter = ColoredFormatter('%(levelname)s %(message)s')

log_file_path = '/var/log/bs_client/bs_client.log'
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(info_color_formatter)

error_file_handler = logging.FileHandler(log_file_path)
error_file_handler.setFormatter(error_color_formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(info_color_formatter)

info_logger.addHandler(info_color_formatter)
info_logger.addHandler(file_handler)

error_logger.addHandler(error_color_formatter)
error_logger.addHandler(error_file_handler)

info_logger.info(f'Le serveur tourne sur {host}:{port}')

try:
    s.connect((host, port))
    info_logger.info(f"Connexion réussie à {host}:{port}.")
    # print(f"Connecté avec succès au serveur {host} sur le port {port}")
except:
    error_logger.error(f"Impossible de se connecter au serveur {host} sur le port {port}.")
    

message = input("Que veux-tu envoyer au serveur : ")

if type(message) is not str:
    raise TypeError("Ici on veut que des strings !")
    
is_meo_or_waf_pattern = re.compile('.*?((meo)|(waf))')

if not is_meo_or_waf_pattern.match(message):
    raise TypeError("L'entrée doit contenir soit 'meo' soit 'waf'")
    
s.sendall(bytes(message, 'utf-8'))

info_logger.info(f"Message envoyé au serveur {host} : {message}.")

server_response = s.recv(1024).decode()

info_logger.info(f"Réponse reçue du serveur {host} : {server_response}.")
# print(f"{server_response}")

s.close()

exit(0)
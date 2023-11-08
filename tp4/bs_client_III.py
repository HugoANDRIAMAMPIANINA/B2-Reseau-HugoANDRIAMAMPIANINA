import socket
from sys import exit
import re
import logging
from color_formatter import ColoredFormatter


host = '10.1.1.11'
port = 12345

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

print("La meilleure calculatrice du monde\n")

calculation = input("Veuillez saisir votre calcul : ")

if type(calculation) is not str:
    raise TypeError("Veuillez saisir un calcul valide")

is_calculation_valid_pattern = re.compile('^(\+|-)?([0-9]){1,5} (\+|-|\*) (\+|-)?([0-9]){1,5}$')

if not is_calculation_valid_pattern.match(calculation):
    raise TypeError("Veuillez saisir un calcul valide (addition, soustraction ou multiplication) : choisir des nombres entiers compris entre -100000 et 100000")

s.sendall(bytes(calculation, 'utf-8'))

logger.info(f"Calcul envoyé au serveur {host} : {calculation}.")

result = s.recv(1024).decode()

print(f"{calculation} = {result}")

logger.info(f"Résultat reçu du serveur {host} : {result}.")

s.close()

exit(0)
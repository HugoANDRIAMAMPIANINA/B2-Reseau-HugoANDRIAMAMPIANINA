import socket
from sys import exit
import re

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except:
    print("Il y a eu un problème pour se connecter au serveur snif")
    

message = input("Que veux-tu envoyer au serveur : ")

if type(message) is not str:
    raise TypeError("Ici on veut que des strings !")
    
is_meo_or_waf_pattern = re.compile('.*?((meo)|(waf))')

if not is_meo_or_waf_pattern.match(message):
    raise TypeError("L'entrée doit contenir soit 'meo' soit 'waf'")
    
s.sendall(bytes(message, 'utf-8'))

server_response = s.recv(1024)

print(f"{server_response.decode()}")

s.close()

exit(0)
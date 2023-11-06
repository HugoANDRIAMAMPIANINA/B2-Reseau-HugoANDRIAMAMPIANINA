import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except:
    print("Il y a eu un problème pour se connecter au serveur snif")

data = s.recv(1024)

print(f"{data.decode()}")

message = input("Que veux-tu envoyer au serveur : ")
s.sendall(bytes(message, 'utf-8'))

server_response = s.recv(1024)

print(f"{server_response.decode()}")

s.close()

exit(0)
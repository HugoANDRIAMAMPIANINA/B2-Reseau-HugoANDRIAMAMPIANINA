import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

data = s.recv(1024)

print(f"{data.decode()}")

s.sendall(b'Meooooo !')

s.close()

exit(0)
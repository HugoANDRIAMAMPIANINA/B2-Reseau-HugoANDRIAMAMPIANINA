import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b'Meooooo !')

try:
    data = s.recv(1024)

    if not data: exit(0)

    print(f"{data}")

except socket.error:
    print("Error Occured.")

s.close()
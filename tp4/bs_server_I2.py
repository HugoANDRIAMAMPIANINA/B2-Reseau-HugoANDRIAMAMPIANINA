import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

conn, addr = s.accept()

print(f"Un client vient de se co et son IP c'est {addr[0]}")

conn.sendall(b'Hi mate!')

while True:

    try:
        data = conn.recv(1024)
        
        if not data: break

        print(f"{data.decode()}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
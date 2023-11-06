import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

while True:
    
    conn, addr = s.accept()

    conn.sendall(b'Hi mate!')

    try:
        data = conn.recv(1024)
        
        if not data: continue

        print(f"{data.decode()}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
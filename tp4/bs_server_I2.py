import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

while True:
    
    conn, addr = s.accept()

    print(f"Un client vient de se co et son IP c'est {addr[0]}")

    conn.sendall(b'Hi mate!')

    try:
        data = conn.recv(1024).decode()
        
        if not data: continue

        print(f"{data}")
        
        if "meo" in data:
            conn.sendall(bytes('Meo à toi confrère.', 'utf-8'))
        elif "waf" in data:
            conn.sendall(b'ptdr t ki')
        else:
            conn.sendall(b'Mes respects humble humain.')

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)
import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

conn, addr = s.accept()

conn.sendall(b'Hi mate!')

while True:

    try:
        data = conn.recv(1024)

        if not data: pass

        print(f"{data.decode()}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()

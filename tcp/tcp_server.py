import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print(f'Connection address:{addr}')

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            print('No data received.')
            break
        print(f"received data:{data.decode()}")
        conn.send("pong".encode())

    conn.close()

listen_forever()
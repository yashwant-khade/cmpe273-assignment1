import socket
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "pong"


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(10)

    print(f'Server at port:{TCP_PORT}')
    output_file = open("tcp_server_out.txt", "a")
    output_file.write(f'Server at port:{TCP_PORT}')
    output_file.write("\n")
    output_file.close()

    while True:
        conn, addr = s.accept()
        Thread(target=execute_thread, args=(conn, addr, BUFFER_SIZE)).start()


def execute_thread(conn, addr, buffer_size):
    data = conn.recv(buffer_size)
    client_data = data.decode().split(",")
    print("Connected client: ", client_data[0])
    output_file = open("tcp_server_out.txt", "a")
    output_file.write("Connected client: " + client_data[0])
    output_file.write("\n")
    output_file.close()
    while True:
        if "end" in client_data:
            conn.close()
            print(f'Connection closed at address: {addr}')
            break
        else:
            output_file = open("tcp_server_out.txt", "a")
            print(f"Received data {client_data[0]} : {client_data[1]}")
            output_file.write(f"Received data {client_data[0]} : {client_data[1]}")
            output_file.write("\n")
            output_file.close()
            conn.send(f"{MESSAGE}".encode())
        data = conn.recv(buffer_size)
        client_data = data.decode().split(",")


listen_forever()

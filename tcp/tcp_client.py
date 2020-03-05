import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"
output_file = open("tcp_clients_out.txt", "a")


def send():
    arguments = sys.argv
    client_id = arguments[1]
    delay = int(arguments[2])
    number_of_pings = int(arguments[3])
    count = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    while count <= number_of_pings:
        print("Sending message: ", MESSAGE)
        output_file.write("Sending message: " + MESSAGE)
        output_file.write("\n")

        sock.send(f"{client_id}, {MESSAGE}".encode())
        data = sock.recv(BUFFER_SIZE)
        print("Received data: ", data.decode())
        output_file.write("Received data: " + data.decode())
        output_file.write("\n")
        count += 1
        time.sleep(delay)
    sock.send("end".encode())
    sock.close()


send()

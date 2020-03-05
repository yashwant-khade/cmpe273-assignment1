import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"
output_file = open('udp_server_out.txt', 'w+')
uploaded_data_file = open("uploaded_file.txt", "w+")


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))

    print(f"Server started at port {UDP_PORT}.")
    output_file.write(f"Server started at port {UDP_PORT}.")
    output_file.write("\n")

    while True:
        data, ip = s.recvfrom(BUFFER_SIZE)
        received_data = data.decode(encoding="utf-8").strip()
        sp = received_data.split(':')
        uploaded_data_file.write(received_data)
        uploaded_data_file.write('\n')
        packet_id = sp[0]
        if packet_id == 'begin':
            print("Accepting a file upload...")
            output_file.write("Accepting a file upload...")
            output_file.write("\n")
        if packet_id == 'end':
            print("Upload successfully completed!")
            output_file.write("Upload successfully completed!")
            output_file.write("\n")

        s.sendto(packet_id.encode(), ip)


listen_forever()

# def listen_forever():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(("", UDP_PORT))
#
#     while True:
#         # get the data sent to us
#         data, ip = s.recvfrom(BUFFER_SIZE)
#         print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
#         # reply back to the client
#         s.sendto(MESSAGE.encode(), ip)

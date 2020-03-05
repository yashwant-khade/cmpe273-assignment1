import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    output_file = open("udp_client_out.txt", "w+")
    print("Connected to the server.")
    output_file.write("Connected to the server.")
    output_file.write('\n')

except socket.error:
    print("Error! {}".format(socket.error))
    exit()


def send(message=''):
    try:
        s.sendto(f"{message}".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        if data.decode() == "begin":
            print("Starting a file (upload.txt) upload...")
            output_file.write("Starting a file (upload.txt) upload...")
            output_file.write("\n")
        if data.decode() == "end":
            print("File uploaded successfully!")
            output_file.write("File uploaded successfully!")
            output_file.write("\n")
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()


def upload_packet(packet_id=0, packet_data=''):
    try:
        s.sendto(f"{packet_id}:{packet_data}".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        if str(packet_id) == data.decode():
            print(f"Received ack({packet_id}) from the server.")
            output_file.write(f"Received ack({packet_id}) from the server.")
            output_file.write("\n")
            return True
        else:
            return False

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()


def upload_file():
    file_path = f'upload.txt'
    file = open(file_path, 'r')

    send("begin")
    if file.mode == 'r':
        for i in file.readlines():
            sp = i.strip().split(':', 1)
            packet_id = int(sp[0])
            packet_data = sp[1]
            flag_uploaded = False

            # if acknowledge is not received then resend packet
            while not flag_uploaded:
                flag_uploaded = upload_packet(packet_id, packet_data)
        send("end")



upload_file()

#
# def get_client_id():
#     id = input("Enter client id:")
#     return id

"""
Author: Yiyang (Jessie) Yu
Student ID: 48362858
Username: yyu69
Date: 01/08/2021
"""
import datetime
import os
import socket
import sys

SERVER = '0.0.0.0'

MAGIC_NO = 0x497E
HEADER_SIZE = 5

FILEREQUEST_MAX_SIZE = 1024
FILEREQUEST_TYPE = 1

FILERESPONSE_TYPE = 2


def get_port():
    if len(sys.argv) == 2:
        global PORT
        PORT = int(sys.argv[1])
        print(f"[SUCCESS] Port number {PORT} from server side received")
        check_port()
    else:
        print(
            "[FAIL] Port number from server side missing. \n" +
            "Try run command line again, making sure to add in the end: \n" +
            "- a port number between 1,024 and 64,000 (including)")
        sys.exit(1)


def check_port():
    if PORT < 1024 or PORT > 64000:
        print(
            "[FAIL] Port number must be between 1,024 and 64,000 (including). \n" +
            "Try run command line again, making sure to add in the end: \n" +
            "- a port number between 1,024 and 64,000 (including)")
        sys.exit(1)
    else:
        print(f"[SUCCESS] Port number valid")
        global ADDRESS
        ADDRESS = (SERVER, PORT)


def create_server_socket():
    try:
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[SUCCESS] Created server socket: {server_socket}")
    except OSError as err:
        print(f"[FAIL] Trouble creating socket with error: {err}")
        sys.exit(err)


def bind_socket():
    try:
        server_socket.bind(ADDRESS)
        print("[SUCCESS] Socket binded to address (host, port): ", ADDRESS)
    except socket.error:
        print(f"[FAIL] Socket cannot bind to address (host, port): {ADDRESS}")
        sys.exit(1)


def start_socket_listening():
    try:
        server_socket.listen()
        print("[SUCCESS] Socket is listening")
    except:
        print("[FAIL] Server socket cannot listen")
        server_socket.close()
        sys.exit(1)


def receive_over_socket(client_socket, size):
    try:
        data = client_socket.recv(size)
        print(f"[SUCCESS] Received {data} of type: {type(data)}")
        return data
    except socket.timeout as error:
        print(f"[FAIL] Trouble receiving the FileRequest. Error: {error}")
        return False


def valid_header():
    if MAGIC_NO != (FILEREQUEST_HEADER[0] << 8) + FILEREQUEST_HEADER[1]:
        print(f"[FAIL] Magic No: {MAGIC_NO} does not match header: {(FILEREQUEST_HEADER[0] << 8) + FILEREQUEST_HEADER[1]}"
              f"[FAIL] The received FileRequest is erroneous")
        return False

    if FILEREQUEST_TYPE != FILEREQUEST_HEADER[2]:
        print(f"[FAIL] Type: {FILEREQUEST_TYPE} does not match header: {FILEREQUEST_HEADER[2]}"
              f"[FAIL] The received FileRequest is erroneous")
        return False

    global FILENAME_LENGTH
    FILENAME_LENGTH = (FILEREQUEST_HEADER[3] << 8) + FILEREQUEST_HEADER[4]
    if FILENAME_LENGTH < 1 or FILENAME_LENGTH > 1024:
        print(f"[FAIL] File name length ({FILENAME_LENGTH}) must be between 1 - 1024 including"
              f"[FAIL] The received FileRequest is erroneous")
        return False

    else:
        print(f"[SUCCESS] FileRequest Header pass all condition checks")
        return True


def check_length():
    if len(FILEREQUEST) != FILENAME_LENGTH:

        print(f"[FAIL] File Request length ({len(FILEREQUEST)}) does not make the length specified in the header ({FILENAME_LENGTH})")
    else:
        print(f"[SUCCESS] File Request length ({len(FILEREQUEST)}) matches specifications in the header ({FILENAME_LENGTH})")


def read_file():
    global STATUS_CODE
    global DATA
    try:
        FileRequest_decoded = FILEREQUEST.decode('utf-8')
        print(f"[SUCCESS] FileRequest Decoded: {FileRequest_decoded}")
        DATA = open('server/' + FileRequest_decoded, 'rb')
        print(f"[SUCCESS] Read {DATA} from {FILEREQUEST}")
        STATUS_CODE = 1
        return True
    except OSError as error:
        print(f"[FAIL] {FILEREQUEST} is erroneous. Error: {error}")
        STATUS_CODE = 0
        return False


def prepare_FileResponse():
    FileResponse = bytearray()

    FileResponse.append(MAGIC_NO >> 8)
    FileResponse.append(MAGIC_NO & 0x00FF)

    FileResponse.append(FILERESPONSE_TYPE)

    FileResponse.append(STATUS_CODE >> 8)
    FileResponse.append(STATUS_CODE & 0x00FF)

    get_data_length()
    FileResponse.append(DATA_LENGTH >> 24)
    FileResponse.append((DATA_LENGTH  & 0x00FF0000) >> 16)
    FileResponse.append((DATA_LENGTH  & 0x0000FF00) >> 8)
    FileResponse.append(DATA_LENGTH  & 0x000000FF)

    return FileResponse


def get_data_length():
    global DATA_LENGTH
    if STATUS_CODE == 1:
        current_working_directory = os.getcwd()
        path = current_working_directory + '/server/' + FILEREQUEST.decode('utf-8')
        DATA_LENGTH = os.path.getsize(path)
        # DATA_LENGTH = len(DATA).to_bytes(4, byteorder='big')
    if STATUS_CODE == 0:
        DATA_LENGTH = 0x0


def send_over_socket(client_socket, data):
    try:
        client_socket.send(data)
        print(f"[SUCCESS] Sent over socket the data: {data} with type: {type(data)}")
    except socket.error:
        print(f"[FAIL] Trouble sending data: {data}")
        client_socket.close()
        sys.exit(1)

def main():
    get_port()

    create_server_socket()
    bind_socket()
    start_socket_listening()

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        client_socket, address = server_socket.accept()
        client_socket.settimeout(1)
        print(f"[SUCCESS] Current time: {datetime.datetime.now().time()}")
        print(f"[SUCCESS] Connection from {address} has been establish")

        global FILEREQUEST_HEADER
        FILEREQUEST_HEADER = receive_over_socket(client_socket, HEADER_SIZE)
        if not FILEREQUEST_HEADER:
            client_socket.close()
            continue # go back to start of loop

        if not valid_header():
            client_socket.close()
            continue  # go back to start of loop

        global FILEREQUEST
        FILEREQUEST = receive_over_socket(client_socket, FILEREQUEST_MAX_SIZE)
        if not FILEREQUEST:
            client_socket.close()
            continue # go back to start of loop

        check_length()

        if not read_file():
            client_socket.close()
            continue

        FileResponse = prepare_FileResponse()
        send_over_socket(client_socket, FileResponse)


if __name__ == '__main__':
    main()

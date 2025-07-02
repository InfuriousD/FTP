import socket
import os

def send_file(connection, filename):
    try:
        with open(filename, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                connection.send(chunk)
        print("File is sent")
    except FileNotFoundError:
        print("File not shown")


def receive_file(connection, filename):
    try:
        with open(filename, "wb") as file:
            while True:
                chunk = connection.recv(1024)
                if not chunk:
                    break
                file.write(chunk)
        print("File received")
    except:
        print("Error in file")


def handle_client(connection):
    while True:
        command = connection.recv(1024).decode()
        if not command:
            break
        if command.startswith("get"):
            filename = command.split()[1]
            send_file(connection, filename)

        if command.startswith("upload"):
            filename = command.split()[1]
            receive_file(connection, 'new_' + filename)

    connection.close()


server_port = 5106
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", server_port))
server_socket.listen(1)
print("FTP Server is listening on port", server_port)
while True:
    connection_socket, adr = server_socket.accept()
    print("Connection established with", adr)
    handle_client(connection_socket)

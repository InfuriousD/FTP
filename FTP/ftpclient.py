import socket
import os
import sys

def receive_file(connection, filename):
    try:
        with open(filename, "wb") as file:
            while True:
                chunk = connection.recv(1024)
                if len(chunk) < 1024:
                    file.write(chunk)
                    break
                file.write(chunk)
        print("File received successfully")
        return True
    except:
        print("Error receiving file")
        return False

def send_file(connection, filename):
    try:
        with open(filename, "rb") as file:
            while True:
                chunk = file.read(1024)
                if len(chunk) < 1024:
                    connection.send(chunk)
                    break
                connection.send(chunk)
        print("File sent successfully")
        return True
    except FileNotFoundError:
        print("File not found")
        return False


server_address = 'localhost'
server_port = int(sys.argv[1])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

while True:
    command = input("Enter command: ")
    client_socket.send(command.encode())
    
    if command.startswith("get"):
        filename = command.split()[1]
        if receive_file(client_socket, "new_" + filename):
            continue
    
    elif command.startswith("upload"):
        filename = command.split()[1]
        if send_file(client_socket, filename):
            continue
        

    client_socket.close() 

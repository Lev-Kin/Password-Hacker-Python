import sys
import socket


def main():
    if len(sys.argv) != 4:
        print("Usage: python hack.py <IP address> <port> <message>")
        return

    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, port))

        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.close()
    except ConnectionRefusedError:
        print("Connection failed!")


if __name__ == "__main__":
    main()

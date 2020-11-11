import time
import socket
import sys

buffer = 1024
host = '127.0.0.1'
port = 8888


def send_msg(sock):
    global buffer
    while True:
        sock.send(bytes(str.encode('test')))
        msg = sock.recv(buffer)
        print(msg.decode('utf-8'))
        time.sleep(2)


def main():
    global host
    global port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        send_msg(sock)


if __name__ == "__main__":
    main()

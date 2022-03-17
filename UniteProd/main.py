# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
import socket
import json

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

m = b'{"id": 2, "name": "abc"}'
jsonObj = json.loads(m)
data = jsonObj

if __name__ == '__main__':
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("BEFORE CONNECT")
            s.connect((HOST, PORT))
            print("AFTER CONNECT")
            s.sendall(m)
            received = s.recv(1024)

        print(f"Sent:     {json.loads(m)}")
        print(f"Received: {json.loads(received)}")
        sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

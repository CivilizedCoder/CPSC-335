import socket
from threading import Thread

def checkPort(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("port",port, "success")
        s.close()
    except Exception as e:
        print(e)

def main():
    address = "192.168.0.100"
    for port in range(201):
        t = Thread(target=checkPort, args=(address, port,))
        t.start()
main()

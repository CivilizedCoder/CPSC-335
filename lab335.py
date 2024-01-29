import socket
from threading import Thread

def test_ip_address(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(100) #arbitrary, didn't want timeout.
        s.connect((ip, port))
        print(f"{ip} success", flush=True)
        s.close()
    except Exception as e:
        print(f"{ip} {e}", flush=True) #would do this differently if I had more time

def main():
    ip_prefix = "192.168.0."
    port = 80
    for i in range(256):
        ip = ip_prefix + str(i)
        t = Thread(target=test_ip_address, args=(ip, port,))
        t.start()

if __name__ == "__main__":
    main()

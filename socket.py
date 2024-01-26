from threading import Thread
import time
import socket
import sys

def worker(id):
	for i in range(256):
		connect(" 192.168.56."+str(i))




def main():
		t = Thread(target=worker, args=(1,))
		t.start()
		
		
def connect(address):
    print(address)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address,80))
        sys.stdout.write('%')
        s.close()
    except Exception as e:
        sys.stdout.write("Caught exception " + str(e)+ "\n")
main()

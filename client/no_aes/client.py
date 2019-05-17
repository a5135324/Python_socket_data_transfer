import time
import socket

def connect_to_server(host, port):
    s = socket.socket()
    s.connect((host, port))
    return s

def send_filename(s, filename):
    #print(filename)
    s.send(filename)
    print('File name send finish!')
    time.sleep(1)

def send_file(s, filename):
    with open(filename, 'rb') as r:
        print('File opened!')
        while True:
            data = r.read(1023)
            #print(data)
            if not data:
                s.send(data)
                break
            #print(data)
            #time.sleep(0.01)
            s.send(data)

        print('File send finish!')

if __name__ == "__main__":
    #host = '127.0.0.1'
    host = '172.17.0.2'
    port = 50000
    filename = b'ubuntu1804.iso'
    s = connect_to_server(host, port)
    send_filename(s, filename)
    send_file(s, filename)
    s.close()

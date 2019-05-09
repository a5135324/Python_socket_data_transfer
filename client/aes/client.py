import time
import socket
from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + str.encode((BS - len(s) % BS) * chr(BS - len(s) % BS))

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def connect_to_server(host, port):
    s = socket.socket()
    s.connect((host, port))
    return s

def send_filename(s, filename):
    pad_name = pad(filename)
    cipher_filename = cipher.encrypt(pad_name)
    #print(cipher_filename)
    s.send(cipher_filename)
    print('File name send finish!')
    time.sleep(1)

def send_file(s, filename):
    with open(filename, 'rb') as r:
        print('File opened!')
        while True:
            data = r.read(4095)
            #print(data)
            if not data:
                break
            #print(data)
            #time.sleep(0.01)
            pad_data = pad(data)
            cipher_data = cipher.encrypt(pad_data)
            s.send(cipher_data)

        print('File send finish!')

if __name__ == "__main__":
    #host = '127.0.0.1'
    host = '172.17.0.2'
    port = 50000
    BS = AES.block_size
    key = 'This is my key!!'
    iv = '1234567890123456'
    #filename = b'test_file'
    filename = b'123'
    #filename = b'ubuntu1804.iso'
    cipher = AES.new(key, AES.MODE_ECB)
    #while True:
    s = connect_to_server(host, port)
    send_filename(s, filename)
    send_file(s, filename)
    s.close()

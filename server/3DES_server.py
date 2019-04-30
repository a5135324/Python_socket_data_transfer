import time
import socket
from Crypto.Cipher import DES3

def pad(s):
    return s + str.encode((BS - len(s) % BS) * chr(BS - len(s) %BS))

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def create_server(host, port):
    s = socket.socket()
    s.bind((host, port))
    s.listen(10)
    print('Server now listening!!')
    return s

def receive_data(s):
    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)

        t0 = time.time()
    
        cipher_name = conn.recv(1032)
        name = cipher.decrypt(cipher_name)
        unpad_name = unpad(name)

        with open(unpad_name, 'wb') as w:
            while True:
                cipher_data = conn.recv(1032)
                if not cipher_data:
                    break
                #print(cipher_data)
                data = cipher.decrypt(cipher_data)
                unpad_data = unpad(data)
                #print(unpad_data)
                w.write(unpad_data)
        print( 'Transfer file use ' + (time.time()-t0-1).__str__() + ' seconds.')
        print('Finish')
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 50000
    BS = DES3.block_size
    key = 'This is my key!!'
    cipher = DES3.new(key, DES3.MODE_ECB)
    s = create_server(host, port)
    receive_data(s)


import os
import time
import socket
from Crypto.Cipher import AES

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def create_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print('Server now listening!!')
    return s

def receive_data(s):
    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)

        cipher_name = conn.recv(1024)
        name = cipher.decrypt(cipher_name)
        unpad_name = unpad(name)
    
        t0 = time.time()
        with open(unpad_name, 'wb') as w:
            while True:
                cipher_data = conn.recv(buf_size)
                length = len(cipher_data)
                if not cipher_data:
                    break
                elif length == buf_size:
                    data = cipher.decrypt(cipher_data)
                    unpad_data = unpad(data)
                    w.write(unpad_data)
                else:
                    while True:
                        length = len(cipher_data)
                        other_data = conn.recv(buf_size - length)
                        if not other_data:
                            data = cipher.decrypt(cipher_data)
                            unpad_data = unpad(data)
                            w.write(unpad_data)
                            break
                        else:
                            cipher_data = cipher_data + other_data
                            if len(cipher_data) == buf_size:
                                data = cipher.decrypt(cipher_data)
                                unpad_data = unpad(data)
                                w.write(unpad_data)
                                break

        all_time = time.time() - t0 - 1 

        print('Transfer file use ' + str(all_time) + ' seconds.')
        print('Finish')
        if os.path.exists(unpad_name):
            os.remove(unpad_name)
            print('delete finish')
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 50000
    BS = AES.block_size
    key = 'This is my key!!'
    buf_size = 153600 
    cipher = AES.new(key, AES.MODE_ECB)
    s = create_server(host, port)
    receive_data(s)


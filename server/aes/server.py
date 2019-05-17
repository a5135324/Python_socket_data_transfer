import time
import socket
from Crypto.Cipher import AES

def pad(s):
    return s + str.encode((BS - len(s) % BS) * chr(BS - len(s) %BS))

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def create_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print('Server now listening!!')
    return s

def decrypt_data(cipher_data, w):
    data = cipher.decrypt(cipher_data)
    unpad_data = unpad(data)
    w.write(unpad_data)

def receive_data(s):
    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)

        cipher_name = conn.recv(1024)
        name = cipher.decrypt(cipher_name)
        unpad_name = unpad(name)
    
        t0 = time.time()
        #a = 0
        with open(unpad_name, 'wb') as w:
          while True:
                cipher_data = conn.recv(1024)
                #a = a + 1
                #print('len = ' + str(len(cipher_data)))
                #if len(cipher_data) % BS != 0:
                #    print(cipher_data)
                
                length = len(cipher_data)
                if not cipher_data:
                    break
                elif length == 1024:
                    #decrypt_data(cipher_data, w)
                    
                    data = cipher.decrypt(cipher_data)
                    unpad_data = unpad(data)
                    w.write(unpad_data)
                else:
                    other_data = conn.recv(1024 - length)
                    mix_data = cipher_data + other_data
                    #print('mix_data len = ' , len(mix_data))
                    #decrypt_data(mix_data, w)
                    data = cipher.decrypt(mix_data)
                    unpad_data = unpad(data)
                    w.write(unpad_data)

        all_time = time.time() - t0 - 1 # - a * 0.1

        print('Transfer file use ' + str(all_time) + ' seconds.')
        print('Finish')
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 50000
    BS = AES.block_size
    key = 'This is my key!!'
    cipher = AES.new(key, AES.MODE_ECB)
    s = create_server(host, port)
    receive_data(s)


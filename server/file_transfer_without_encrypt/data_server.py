import socket
import time
from Crypto.Cipher import AES

s = socket.socket()
host = '0.0.0.0'
port = 50000

s.bind((host, port))
s.listen(10)
print('Server now listening!')

obj = AES.new('This is my key!!', AES.MODE_CBC, 'IV is 1234567890')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    
    t0 = time.time()
    
    message = conn.recv(1024)
    
    print(message)

    plaintext = obj.decrypt(message)
    print(plaintext)

    '''
    filename = conn.recv(1024).decode('ISO-8859-1')
    print(filename)
    filename = filename.strip('\n')
    with open(filename, 'wb') as w:
        while True:
            #try:
            data = conn.recv(1024)
            if not data:
                break
            w.write(data)
            #except BaseException:
             #   print('error')
    
    print( 'Transfer file use ' + (time.time()-t0-1).__str__() + ' seconds.')
    print('Finish')
    '''
    conn.close()

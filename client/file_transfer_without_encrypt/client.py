import socket
import time
from Crypto.Cipher import AES

#host = '172.17.0.2'
host = '127.0.0.1'
port = 50000

s = socket.socket()
s.connect((host, port))

obj = AES.new('This is my key!!', AES.MODE_CBC, 'IV is 1234567890')

ciphertext = obj.encrypt('This is plaintex')
#filename = 'SafeBricks.pdf'
#filename = 'ubuntu1804.iso'
#s.send(str.encode(filename+'\n'))
s.send(ciphertext)
print(ciphertext)

time.sleep(1)
'''
with open(filename, 'rb') as r:
    print('File opened')
    while True:
        data = r.read()
        if not data:
            s.send(data)
            break
        s.send(data)

    print('Done!')
'''
s.close()


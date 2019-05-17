import time
import socket

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

        name = conn.recv(1024)
    
        t0 = time.time()
        #a = 0
        with open(name, 'wb') as w:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #print(data)
                #print('len = ' , len(data))
                w.write(data)
        all_time = time.time() - t0 - 1

        print('Transfer file use ' + str(all_time) + ' seconds.')
        print('Finish')
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 50000
    s = create_server(host, port)
    receive_data(s)


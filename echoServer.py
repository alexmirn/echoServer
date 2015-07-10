# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys

class EchoServer(object):
    
    def __init__(self, port=9090):
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.running = False
       
    def isRunning(self):
        return self.running
        
    def start(self):
        self.isRunning = True
        self.sock.bind(('', self.port))
        self.sock.listen(2)
        print 'Server started work at port:', self.port
        
        conn, addr = self.sock.accept()
        print 'This client connected:', addr

        while True:
            inData = conn.recv(1024)
            conn.send(inData)

            if inData.split()[0] == 'disconnect':
                # self.sock.close()
                conn.close()
                break
        
    def stop(self):
        self.isRunning = False
        # conn.close()
        self.sock.close()

if __name__ == '__main__':
    sock1 = EchoServer(8866)
    
    sock1.start()
    sock1.stop()



# import socket
# import thread

# def handle(client_socket, address):
#     while True:
#         data = client_socket.recv(512)
#         if data.startswith("exit"): # if data start with "exit"
#             client_socket.close() # close the connection with the client
#             break
#         client_socket.send(data) # echo the received string

# # opening the port 1075
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('',1093))
# server.listen(10)

# while True: # listen for incoming connections
#     client_socket, address = server.accept()
#     print "request from the ip",address[0]
#  # spawn a new thread that run the function handle()
#     thread.start_new_thread(handle, (client_socket, address)) 




# import threading

# def writer(x, event_for_wait, event_for_set):
#     for i in xrange(10):
#         event_for_wait.wait() # wait for event
#         event_for_wait.clear() # clean event for future
#         print x
#         event_for_set.set() # set event for neighbor thread

# # init events
# e1 = threading.Event()
# e2 = threading.Event()

# # init threads
# t1 = threading.Thread(target=writer, args=(0, e1, e2))
# t2 = threading.Thread(target=writer, args=(1, e2, e1))

# # start threads
# t1.start()
# t2.start()

# e1.set() # initiate the first event

# # join threads to the main thread
# t1.join()
# t2.join()
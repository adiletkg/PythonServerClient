from selenium import webdriver
from socket import *
from time import ctime
HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSer=socket(AF_INET,SOCK_STREAM)
tcpSer.bind(ADDR)
tcpSer.listen(5)

while True:
    print 'waiting for connection...'
    tcpCli, address=tcpSer.accept()
    print '...connected from:', address

    while True:
        data=tcpCli.recv(BUFSIZE)
        if not data:
            break
        tcpCli.send('[%s] %s' %(ctime(),data))

    tcpCli.close()
tcpSer.close()











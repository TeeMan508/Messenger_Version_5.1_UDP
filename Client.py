from socket import *
import sys

host = '192.168.0.70'
port = 9090
addr = (host,port)

udp_socket = socket(AF_INET, SOCK_DGRAM)
name = input('Input Your Name: ')
while True:
    data = input('write to server: ')
    if data != '':
        data = str.encode(name + ' sended: ' + data)
        udp_socket.sendto(data, addr)
        data = bytes.decode(data)
        data = udp_socket.recvfrom(1024)
        print(data)
    else:
        data = input('write to server: ')



udp_socket.close()
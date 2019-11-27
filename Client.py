from socket import *

host = gethostbyname(gethostname())
port = 9090
addr = (host,port)
quit = False
udp_socket = socket(AF_INET, SOCK_DGRAM)
name = input('Input Your Name: ')
while not quit:
    data = input('write to server: ')
    if data != '':
        if data == 'end':
            data = str.encode(name + ' disconnected')
            udp_socket.sendto(data, addr)
            quit = True
            print('Disconnected from server')
        data = str.encode(name + ' sended: ' + data)
        udp_socket.sendto(data, addr)
        data = bytes.decode(data)
        data = udp_socket.recvfrom(1024)
        print(data)
    else:
        data = input('write to server: ')



udp_socket.close()
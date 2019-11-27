from socketserver import *

host = 'localhost'
port = 777
addr = (host, port)

class MyUDPHandler(DatagramRequestHandler):

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        print(data)
        socket.sendto(data, self.client_address)


if __name__ == "__main__":
    server = UDPServer(addr, MyUDPHandler)
    print('[Server Started]')
    server.serve_forever()

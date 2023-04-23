from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class UDPServer(DatagramProtocol):

    def datagramReceived(self, datagram, address):
        print(f"Received {datagram.hex()} from {address}")  

if __name__ == '__main__':
    reactor.listenUDP(7777, UDPServer())
    reactor.run()
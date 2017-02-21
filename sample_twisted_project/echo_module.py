"""
-Echo Protocols and Factories for use with twisted applications and plugins
"""

from twisted.internet import protocol, reactor

class EchoServerProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return EchoServerProtocol()

class EchoClientProtocol(protocol.Protocol):
   def connectionMade(self):
       self.transport.write("Hello, world!")

   def dataReceived(self, data):
       print "Server said:", data
       self.transport.loseConnection()

class EchoClientFactory(protocol.ClientFactory):
   def buildProtocol(self, addr):
       return EchoClientProtocol()

   def clientConnectionFailed(self, connector, reason):
       print "Connection failed."
       reactor.stop()

   def clientConnectionLost(self, connector, reason):
       print "Connection lost."
       reactor.stop()

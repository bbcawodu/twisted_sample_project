"""
- Twisted plugin that deploys the TCPChatServerService

- command to start service
    - twistd tcp_chat_server --port=<port number>
- command to stop service
    - kill -INT `cat twistd.pid`
- command to connect to chat server through telnet command line utility
    - telnet localhost <port number>
    - To terminate a telnet connection, hold down the Control key and press
    the right-bracket key. That will drop you to a telnet> prompt; from
    there, type quit and press the Return key to terminate the connection.
"""

from zope.interface import implements

from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
from twisted.python import usage

from sample_twisted_project import TCPChatServerFactory

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to listen on."]]

class TCPChatServerServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "tcp_chat_server"
    description = "A TCP-based chat server."
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in tcp_chat_module.py.
        """
        return internet.TCPServer(int(options["port"]), TCPChatServerFactory())

serviceMaker = TCPChatServerServiceMaker()
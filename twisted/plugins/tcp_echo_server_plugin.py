"""
- Twisted plugin that deploys the TCPEchoServerService

- command to start service
    - twistd tcp_echo_server --port=<port number>
- command to stop service
    - kill -INT `cat twistd.pid`
"""

from zope.interface import implements

from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
from twisted.python import usage

from sample_twisted_project import EchoServerFactory

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to listen on."]]

class TCPEchoServerServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "tcp_echo_server"
    description = "A TCP-based echo server."
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in echo_module.py.
        """
        return internet.TCPServer(int(options["port"]), EchoServerFactory())

serviceMaker = TCPEchoServerServiceMaker()

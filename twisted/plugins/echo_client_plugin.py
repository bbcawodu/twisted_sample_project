# command to start service
# twistd tcp_echo_client --port=<port number>
# command to start service with different pid and log files than the default (useful if server is running on default)
# twistd --pidfile twistd2.pid --logfile twistd2.log tcp_echo_client --port=<port number>

from zope.interface import implements

from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
from twisted.python import usage

from sample_twisted_project import EchoClientFactory

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to connect to."]]

class EchoClientServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "tcp_echo_client"
    description = "A TCP-based echo client."
    options = Options

    def makeService(self, options):
        """
        Construct a TCPClient from a factory defined in echo_module.py.
        """
        return internet.TCPClient("localhost", int(options["port"]), EchoClientFactory())

serviceMaker = EchoClientServiceMaker()

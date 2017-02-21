"""
- Twisted plugin that deploys the HTTPCalendarServerService

- command to start service
    - twistd http_calendar_server --port=<port number>
- command to stop service
    - kill -INT `cat twistd.pid`
"""

from zope.interface import implements
from twisted.application.service import IServiceMaker
from twisted.plugin import IPlugin
from twisted.application import internet
from twisted.python import usage
from twisted.web.server import Site
from sample_twisted_project import CalendarHome

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to listen on."]]

class HTTPCalendarServerServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "http_calendar_server"
    description = "An HTTP-based calendar server."
    options = Options

    def makeService(self, options):
        """
        Construct an HTTP Site Server from a factory defined in calendar_module.py.
        """

        resource = CalendarHome()
        factory = Site(resource)
        return internet.TCPServer(int(options["port"]), factory)

serviceMaker = HTTPCalendarServerServiceMaker()

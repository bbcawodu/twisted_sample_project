"""
- Twisted plugin that deploys the HTTPFormServerService

- command to start service
    - twistd http_post_form_server --port=<port number>
- command to stop service
    - kill -INT `cat twistd.pid`
"""

from zope.interface import implements
from twisted.application.service import IServiceMaker
from twisted.plugin import IPlugin
from twisted.application import internet
from twisted.python import usage
from twisted.web.server import Site
from sample_twisted_project import FormPage

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to listen on."]]

class HTTPFormServerServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "http_post_form_server"
    description = "An HTTP-based form server."
    options = Options

    def makeService(self, options):
        """
        Construct an HTTP Site Server from a factory defined in http_post_form_module.py.
        """

        resource = FormPage()
        factory = Site(resource)
        return internet.TCPServer(int(options["port"]), factory)

serviceMaker = HTTPFormServerServiceMaker()

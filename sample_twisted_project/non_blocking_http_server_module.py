"""
- Non-blocking HTTP server Resource for use with twisted applications and plugins
"""

from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
import time

class BusyPage(Resource):
    isLeaf = True

    def _delayedRender(self, request):
        request.write("Finally done, at %s" % (time.asctime(),))
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET
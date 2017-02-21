# to start:
# twistd -y echo_server.tac
# To stop:
# kill -INT `cat twistd.pid`

from twisted.application import internet, service
from sample_twisted_project import EchoFactory

application = service.Application("echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)

from os import environ
from stub.Stub import Stub


class ApiStub(Stub):
    
    def __init__(self, server):
        super().__init__(server, environ.get('API_QUEUE_NAME'))

    def hello_world(self, content):
        self._send('hello-world', content)

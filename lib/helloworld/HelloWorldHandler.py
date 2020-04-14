
class HelloWorldHandler:
    def __init__(self, api_stub):
        self.primitive_name = 'hello-world'
        self.api_stub = api_stub

    def consume(self, message):
        print(message)
        self.api_stub.hello_world({ 'teste': 'teste' })
        

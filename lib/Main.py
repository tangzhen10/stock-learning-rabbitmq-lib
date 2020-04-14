from os import environ
from dotenv import load_dotenv
from helloworld.HelloWorldHandler import HelloWorldHandler
from RabbitMQ import RabbitMQ
from stub.ApiStub import ApiStub

if __name__ == "__main__":
    load_dotenv()
    server = RabbitMQ(environ.get('QUEUE_NAME'), environ.get('RABBITMQ_CONNECTION_STRING'))
    api_stub = ApiStub(server)

    server.register(HelloWorldHandler(api_stub))

    server.start_listening()

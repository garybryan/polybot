from models import Message
from backends import backend

def post(message: Message):
    reply = backend.send_message(message)
    return reply
